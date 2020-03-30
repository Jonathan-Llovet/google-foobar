def solution(l):
    """Returns the number of access codes that are present in the list l

    The access codes contained in the list l are 'lucky triples'.
    'Lucky triples' are defined as a tuple (x, y, z) where x divides y and y
    divides z, and where the indices (xi, yj, zk) satisfy i < j < k, such as
    (1, 2, 4).

    Args:
        l: List of integers potentially containing access codes

    Returns:
        An integer indicating how many access codes are present in list l
        If no access codes are found, 0 is returned.
    """
    access_codes = 0

    if len(l) < 3:
        return access_codes
    
    calculated = dict({})
    for i in range(len(l)):
        if str(l[i]) not in calculated.keys():
            calculated.update({str(l[i]): [i]})
        else:
            indices = calculated[str(l[i])]
            indices.append(i)
            calculated.update({str(l[i]): indices})
                
    int_keys = [int(key) for key in calculated.keys()]
    unique_values = sorted(int_keys, reverse=True)
    
    secret_key_candidates = []
    for k in unique_values:
        for j in unique_values:
            if k % j == 0:
                if j == 1:
                    i = k
                else:
                    i = k / j
                if i in unique_values:
                    candidate = sorted([i, j, k])
                    if candidate not in secret_key_candidates:
                        secret_key_candidates.append(candidate)
    # iterate over candidates and check indices against calculated
    key_candidates = verify_secret_key_candidate_positions(secret_key_candidates, calculated, (0,1))
    secret_keys = verify_secret_key_candidate_positions(key_candidates, calculated, (1,2))
    access_codes = len(secret_keys)
    return access_codes

def verify_secret_key_candidate_positions(secret_key_candidates, calculated, indices=(0,1)):
    for candidate in secret_key_candidates:
        i_value = candidate[indices[0]]
        j_value = candidate[indices[1]]
        li = calculated[str(i_value)] # list of indices from l
        lj = calculated[str(j_value)]
        keep_candidate = None
        for i_index in li:
            for j_index in lj:
                if i_index < j_index:
                    keep_candidate = True
                    break
            if keep_candidate:
                break
            else:
                secret_key_candidates.remove(candidate)
    return secret_key_candidates
