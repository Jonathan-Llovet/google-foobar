import sys

def solution(l):
    """Returns the number of access codes that are present in the list l

    The access codes contained in the list l are "lucky triples".
    "Lucky triples" are defined as a tuple (x, y, z) where x divides y and y
    divides z, and where the indices (x_i, y_j, z_k) satisfy i < j < k, such as
    (1, 2, 4).

    Args:
        l: List of integers potentially containing access codes

    Returns:
        An integer indicating how many access codes are present in list l
        If no access codes are found, 0 is returned.
    """

    if len(l) < 3:
        return 0
    if len(l) == 3:
        if l.count(l[0]) == 3:
            return 1

    meta = generate_metadata(l)
    candidates = find_access_code_candidates(meta)
    access_codes = remove_bad_code_candidates(meta, candidates)
    num_access_codes = len(access_codes)
    return num_access_codes

def get_indices(l):
    """ Description ...

    Args:
        l: ...

    Returns:
        meta ... For example:

        ...
    """
    meta = dict({})
    for i, k in enumerate(l):
        if k == 0:
            continue
        k_str = str(k)
        if k_str not in meta.keys():
            meta.update({
                k_str: {
                    "indices": [i],
                    "divisors": []
                }
            })
        elif k_str in meta.keys():
            k_indices = meta[k_str]["indices"]
            k_indices.append(i)
            k_divisors = meta[k_str]["divisors"]

            meta.update({
                k_str: {
                    "indices": k_indices,
                    "divisors": k_divisors
                }
            })
    return meta

def calculate_divisors(meta):
    """ Description ...

    Args:
        l: ...

    Returns:
        meta ... For example:

        ...
    """
    for unique_value in meta.keys():
        k = int(unique_value)
        k_indices = meta[unique_value]["indices"]
        k_divisors = meta[unique_value]["divisors"]
        for divisor_candidate in meta.keys():
            candidate = int(divisor_candidate)
            if k % candidate == 0:
                if candidate not in k_divisors:
                    k_divisors.append(candidate)
        meta.update({
            unique_value: {
                "indices": sorted(k_indices, reverse=True),
                "divisors": k_divisors
            }
        })
    return meta

def generate_metadata(l):
    """ Description ...

    Args:
        l: ...

    Returns:
        meta ... For example:

        ...
    """
    meta_indices = get_indices(l)
    meta = calculate_divisors(meta_indices)
    return meta

def find_access_code_candidates(meta):
    """ Description ...

    Args:
        l: ...

    Returns:
        meta ... For example:

        ...
    """
    candidates = []
    for x, k in meta.iteritems():
        for y in k["divisors"]:
            for z in meta[str(y)]["divisors"]:
                valid = validate_instance_count(meta, x, y, z)
                if valid:
                    if sorted((int(x), y, z)) not in candidates:
                        candidates.append(sorted((int(x), y, z)))
    return candidates

def validate_instance_count(meta, *args):
    """ Description ...

    Args:
        l: ...

    Returns:
        meta ... For example:

        ...
    """
    args = list(map(int, args))
    for item in args:
        if args.count(int(item)) > len(meta[str(item)]["indices"]):
            return False
    return True

def remove_bad_code_candidates(meta, candidates):
    """ Description ...

    Args:
        l: ...

    Returns:
        meta ... For example:

        ...
    """
    access_codes = list(candidates)
    for candidate in candidates:
        candidate_x, candidate_y, candidate_z = list(map(str, candidate))

        x_indices = meta[candidate_x]["indices"]
        y_indices = meta[candidate_y]["indices"]
        z_indices = meta[candidate_z]["indices"]

        if not is_in_order(x_indices, y_indices, z_indices):
            access_codes.remove(candidate)

    return access_codes

def is_in_order(x_indices, y_indices, z_indices):
    """ Description ...

    Args:
        l: ...

    Returns:
        meta ... For example:

        ...
    """
    for x_i in x_indices:
        for y_j in y_indices:
            x_y_in_order = False
            y_z_in_order = False
            if x_i < y_j:
                x_y_in_order = True
            if x_y_in_order:
                for z_k in z_indices:
                    if y_j < z_k:
                        y_z_in_order = True
                        break
            if (x_y_in_order and y_z_in_order):
                break
        if (x_y_in_order and y_z_in_order):
            break
    return x_y_in_order and y_z_in_order
