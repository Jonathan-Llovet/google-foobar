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
        print "returning: {}".format(access_codes)
        return access_codes
    l1 = l
    l2 = sorted(list(set(l1)), reverse=True)
    print "l2: {}".format(l2)
    # candidates = []
    
    # if 1 in l and 1 in l[l.index(1)+1:]:
    #     for k in l2:
    #         if len(l) == 3:
    #             if k == 1:
    #                 continue
    #             print "calling is_in_order(l, 1, 1, {})".format(k)
    #             if is_in_order(l, 1, 1, k):
    #                 print "calling candidates.append((1, 1, {}))".format(k)
    #                 if (1, 1, k) not in candidates:
    #                     candidates.append((1, 1, k))

    candidates = handle_cases_with_1s(l, l2)

    if 1 in l2 and len(l2) < 3:
        if len(l2) == 1:
            print "handling len(l2) == 1"
            print "calling candidates.append((1, 1, 1))"
            candidates.append((1,1,1))
        if len(l2) == 2:
            print "handling len(l2) == 2"
            if 1 in l[l.index(1)+1:]:
                print "handling 1 in l[l.index(1)+1:]"
                print "l: {}".format(l)
                print "is_in_order(l, 1, 1, {})".format(l2[0])
                print str(is_in_order(l, 1, 1, l2[0]))
                if is_in_order(l, 1, 1, l2[0]):
                    print "calling candidates.append((1, 1, {}))".format(l2[0])
                    if (1, 1, l2[0]) not in candidates:
                        candidates.append((1, 1, l2[0]))
            # print "is_in_order(l, 1, {}, {})".format(l2[0], l2[0])
            # print str(is_in_order(l, 1, l2[0], l2[0]))
            elif l2[0] in l[l.index(l2[0])+1:]:
                if is_in_order(l, 1, l2[0], l2[0]):
                    print "calling candidates.append((1, {}, {}))".format(l2[0], l2[0])
                    if (1, l2[0], l2[0]) not in candidates:
                        candidates.append((1, l2[0], l2[0]))
    
    for k in l2:
        print "k: {}".format(k)
        for j in l2:
            print "j: {}".format(j)
            if k % j == 0:
                for i in l2:
                # for i in l2[l2.index(j)+1:]:
                    print "i: {}".format(i)
                    if j % i == 0:
                        i, j, k = sorted([i, j, k])
                        if is_in_order(l, i, j, k):
                            if (i, j, k) not in candidates:
                                print "calling candidates.append(({}, {}, {}))".format(i,j,k)
                                candidates.append((i, j, k))

    # if len(l2) == 1:
    #     if 1 in l2:
    #         candidates.append((1,1,1))
    # if len(l2) == 2:
    #     if 1 in l2:
    #         if is_in_order(l, 1, l2[0], l2[0]):
    #             candidates.append((1, l2[0], l2[0]))
    


    # ////////////////////////
    # elif is_in_order(l, 1, l2[1], l2[2]):
    #     candidates.append((1, l2[1], l2[2]))

    # for k in l2:
    #     for j in l2:
    #         if not k % j == 0:
    #             continue
    #         else:
    #             for i in l2:
    #                 if not j % i == 0:
    #                     continue
    #                     if is_in_order(l, i, j, k):
    #                         if candidate not in candidates:
    #                             candidates.append((i, j, k))
    








    access_codes = len(candidates)
    print "candidates: {}".format(str(candidates))
    print "returning: {}".format(access_codes)
    return access_codes

def handle_cases_with_1s(original_list, unique_values, candidates=[]):
    if 1 in original_list and 1 in original_list[original_list.index(1)+1:]:
            for k in unique_values:
                if len(original_list) == 3:
                    if k == 1:
                        continue
                    if is_in_order(original_list, 1, 1, k):
                        if (1, 1, k) not in candidates:
                            candidates.append((1, 1, k))
    return candidates

def is_in_order(l, x, y, z):
    try:
        print "inside is_in_order"
        print "called with x: {} y: {} z: {}".format(x,y,z)
        print l
        # x_index = l.index(args[0])
        # print x_index
        # for item in list(args)[1:]:
        #     item_index = l.index(args[args.index(item)])
        x_index = l.index(x)
        if x_index == 0:
            y_index = l[x_index + 1:].index(y) + 1
        else:
            y_index = x_index + l[x_index + 1:].index(y) + 1
        z_index = y_index + l[y_index + 1:].index(z) + 1
        print "x_index: {}".format(x_index)
        print "l[x_index:]"
        print l[x_index:]
        print "y_index: {}".format(y_index)
        print "l[y_index:]"
        print l[y_index:]
        print "z_index: {}".format(z_index)
        x_before_y = x_index < y_index
        y_before_z = y_index < z_index
        print "x_before_y: {}".format(x_before_y)
        print "y_before_z: {}".format(y_before_z)
        print "returning: {}".format(x_before_y and y_before_z)
        return x_before_y and y_before_z
    except ValueError as e:
        print e
        print "Value not found in list."
        print "returning: {}".format(False)
        return False
# is_in_order(l,1,1,2)
# is_in_order(l,1,2,2)

def test(l, expected):
    print "solution({})".format(str(l))
    print "************************************************"
    result = solution(l)
    print "************************************************"
    print "expected: {}".format(expected)
    if result == expected:
        print "solution({})".format(str(l))
        print "PASSED"
    else:
        print "solution({})".format(str(l))
        print "FAILED"
    print "\n"


test([1, 1], 0)
test([1, 1, 2], 1)
test([1, 1, 1, 1], 1)
test([1, 1, 2, 1, 1], 2)
test([1, 1, 2, 1, 1, 2], 3)
test([1, 1, 2, 4, 1, 2], 5)
test([1, 1, 2, 1], 2)
test([1, 2, 3, 4, 5, 6], 3)
test([1, 1, 1], 1)
test([2, 2, 2], 1)
test([2, 4, 2], 0)
test([2, 4, 12], 1)
test([2, 4, 8], 1)
test([2, 4, 8, 12, 16], 5)
test([6,5,3,2,1], 0)
test([], 0)
test([3,2,5,2,1,6,8],2)
test([31, 31, 1, 4, 2, 62], 2)