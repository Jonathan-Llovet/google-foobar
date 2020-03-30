import random
import timeit
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
    l1 = l
    l2 = sorted(list(set(l1)), reverse=True)
    candidates = []
    
    if 1 in l and 1 in l[l.index(1)+1:]:
        for k in l2:
            if len(l) == 3:
                if k == 1:
                    continue
                if is_in_order(l, 1, 1, k):
                    if (1, 1, k) not in candidates:
                        candidates.append((1, 1, k))

    if 1 in l2 and len(l2) < 3:
        if len(l2) == 1:
            candidates.append((1,1,1))
        if len(l2) == 2:
            if 1 in l[l.index(1)+1:]:
                if is_in_order(l, 1, 1, l2[0]):
                    if (1, 1, l2[0]) not in candidates:
                        candidates.append((1, 1, l2[0]))
            elif l2[0] in l[l.index(l2[0])+1:]:
                if is_in_order(l, 1, l2[0], l2[0]):
                    if (1, l2[0], l2[0]) not in candidates:
                        candidates.append((1, l2[0], l2[0]))
    
    for k in l2:
        for j in l2:
            if k % j == 0:
                for i in l2:
                    if j % i == 0:
                        i, j, k = sorted([i, j, k])
                        if is_in_order(l, i, j, k):
                            if (i, j, k) not in candidates:
                                candidates.append((i, j, k))

    access_codes = len(candidates)
    return access_codes

def is_in_order(l, x, y, z):
    try:
        x_index = l.index(x)
        if x_index == 0:
            y_index = l[x_index + 1:].index(y) + 1
        else:
            y_index = x_index + l[x_index + 1:].index(y) + 1
        z_index = y_index + l[y_index + 1:].index(z) + 1
        x_before_y = x_index < y_index
        y_before_z = y_index < z_index
        return x_before_y and y_before_z
    except ValueError:
        return False
