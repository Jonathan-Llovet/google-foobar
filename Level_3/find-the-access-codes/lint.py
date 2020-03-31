def solution(l):
    """Returns the number of access codes that are present in the list l

    The access codes contained in the list l are "lucky triples".
    "Lucky triples" are defined as a tuple (x, y, z) where x divides y and y
    divides z, and where the indices (xi, yj, zk) satisfy i < j < k, such as
    (1, 2, 4).

    Args:
        l: List of integers potentially containing access codes

    Returns:
        An integer indicating how many access codes are present in list l
        If no access codes are found, 0 is returned.
    """

    if len(l) < 3:
        return str(0)

    meta = generate_metadata(l)
    candidates = find_access_code_candidates(meta)
    access_codes = remove_bad_code_candidates(meta, candidates)
    return str(len(access_codes))

def get_indices(l):
    meta = dict({})
    for i, k in enumerate(l):
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
    meta_indices = get_indices(l)
    meta = calculate_divisors(meta_indices)
    return meta

def find_access_code_candidates(meta):
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
    args = list(map(int, args))
    for item in args:
        if args.count(int(item)) > len(meta[str(item)]["indices"]):
            return False
    return True

def remove_bad_code_candidates(meta, candidates):
    access_codes = list(candidates)
    for candidate in candidates:
        x, y, z = list(map(int, candidate))

        x_indices = meta[str(x)]["indices"]
        y_indices = meta[str(y)]["indices"]
        z_indices = meta[str(z)]["indices"]
        
        for xi in x_indices:
            for yj in y_indices:
                xy_in_order = False
                yz_in_order = False
                if xi < yj:
                    xy_in_order = True
                if xy_in_order:
                    for zk in z_indices:
                        if yj < zk:
                            yz_in_order = True
                            break
                if (xy_in_order and yz_in_order):
                    break
            if (xy_in_order and yz_in_order):
                break
        
        if not (xy_in_order and yz_in_order):
            access_codes.remove(candidate)

    return access_codes
