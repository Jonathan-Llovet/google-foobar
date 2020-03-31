import random
import timeit

# def solution(l):
#     """Returns the number of access codes that are present in the list l

#     The access codes contained in the list l are "lucky triples".
#     "Lucky triples" are defined as a tuple (x, y, z) where x divides y and y
#     divides z, and where the indices (xi, yj, zk) satisfy i < j < k, such as
#     (1, 2, 4).

#     Args:
#         l: List of integers potentially containing access codes

#     Returns:
#         An integer indicating how many access codes are present in list l
#         If no access codes are found, 0 is returned.
#     """

#     if len(l) < 3:
#         return str(0)

#     meta = generate_metadata(l)
#     # print "final: {}".format(meta)
#     candidates = find_access_code_candidates(meta)
#     access_codes = remove_bad_code_candidates(meta, candidates)
#     # print access_codes
#     return str(len(access_codes))

# def get_indices(l):
#     # print "in get_indices..."
#     meta = dict({})
#     for i, k in enumerate(l):
#         k_str = str(k)
#         if k_str not in meta.keys():
#             meta.update({
#                 k_str: {
#                     "indices": [i],
#                     "divisors": []
#                 }
#             })
#         elif k_str in meta.keys():
#             k_indices = meta[k_str]["indices"]
#             k_indices.append(i)
#             k_divisors = meta[k_str]["divisors"]

#             meta.update({
#                 k_str: {
#                     "indices": k_indices,
#                     "divisors": k_divisors
#                 }
#             })
#         # print k_str
#         # print meta
#     # print "end get_indices..."
#     return meta

# def calculate_divisors(meta):
#     # print "in calculate_divisors..."
#     for unique_value in meta.keys():
#         # print "Outer loop unique_value: {}".format(unique_value)
#         k = int(unique_value)
#         k_indices = meta[unique_value]["indices"]
#         k_divisors = meta[unique_value]["divisors"]
#         for divisor_candidate in meta.keys():
#             # print "divisor_candidate: {}".format(divisor_candidate)
#             candidate = int(divisor_candidate)
#             if k % candidate == 0:
#                 # print "k mod candidate == 0: {}".format(k % candidate == 0)
#                 if candidate not in k_divisors:
#                     # print "Appending candidate: {}".format(candidate)
#                     k_divisors.append(candidate)
#                     # print "k_divisors for {}: {}".format(unique_value, k_divisors)
#         # print "k_divisors for {}: {}".format(unique_value, k_divisors)
#         meta.update({
#                 unique_value: {
#                     "indices": sorted(k_indices, reverse=True),
#                     "divisors": k_divisors
#                 }
#             })
#     # print "end calculate_divisors..."
#     return meta

# def generate_metadata(l):
#     # print "in generate_metadata..."
#     meta_indices = get_indices(l)
#     meta = calculate_divisors(meta_indices)
#     # print "end generate_metadata..."
#     return meta


# def find_access_code_candidates(meta):
#     # solution([31, 31, 1, 4, 2, 62])
#     # final: {"1": {"indices": [2], "divisors": [1]}, "62": {"indices": [5], "divisors": [1, 62, 2, 31]}, "2": {"indices": [4], "divisors": [1, 2]}, "4": {"indices": [3], "divisors": [1, 2, 4]}, "31": {"indices": [0, 1], "divisors": [1, 31]}}

#     # solution([1, 1, 2])
#     # final: {"1": {"indices": [0, 1], "divisors": [1]}, "2": {"indices": [2], "divisors": [1, 2]}}
#     candidates = []
#     for x, k in meta.iteritems():
#         # print str(x), str(k)
#         # 1 {"indices": [2], "divisors": [1]}
#         # 62 {"indices": [5], "divisors": [1, 62, 2, 31]}
#         # 2 {"indices": [4], "divisors": [1, 2]}
#         # 4 {"indices": [3], "divisors": [1, 2, 4]}
#         # 31 {"indices": [0, 1], "divisors": [1, 31]}        
#         for y in k["divisors"]:
#             for z in meta[str(y)]["divisors"]:
#                 valid = validate_instance_count(meta, x, y, z)
#                 if valid:
#                     if sorted((int(x), y, z)) not in candidates:
#                         candidates.append(sorted((int(x), y, z)))
    
#     # print "candidates: {}".format(candidates)
#     return candidates

# def validate_instance_count(meta, *args):
#     # print "in validate_instance_count"
#     args = list(map(int, args))
#     # print "args: {}".format(args)
#     for item in args:
#         # print "item: {}".format(item)
#         # print "args.count(int(item)): {}".format(args.count(int(item)))
#         # print 'meta[str(item)]["indices"]: {}'.format(meta[str(item)]["indices"])
#         if args.count(int(item)) > len(meta[str(item)]["indices"]):
#             return False
#     return True

# def remove_bad_code_candidates(meta, candidates):  
#     # print "in remove_bad_code_candidates"
#     # print "candidates: {}".format(candidates)
#     access_codes = list(candidates)
#     for candidate in candidates:
#         # print "candidate: {}".format(candidate)
#         # 1 {"indices": [2], "divisors": [1]}
#         # 62 {"indices": [5], "divisors": [1, 62, 2, 31]}
#         # 2 {"indices": [4], "divisors": [1, 2]}
#         # 4 {"indices": [3], "divisors": [1, 2, 4]}
#         # 31 {"indices": [0, 1], "divisors": [1, 31]}      
#         x, y, z = list(map(int, candidate))

#         # print "x: {}".format(x)
#         # print "y: {}".format(y)
#         # print "z: {}".format(z)

#         x_indices = meta[str(x)]["indices"]
#         y_indices = meta[str(y)]["indices"]
#         z_indices = meta[str(z)]["indices"]

#         # print "x_indices: {}".format(x_indices)
#         # print "y_indices: {}".format(y_indices)
#         # print "z_indices: {}".format(z_indices)

#         # yx_in_order = False
#         # zy_in_order = False

        
#         # print "Checking indices..."
#         for xi in x_indices:
#             for yj in y_indices:
#                 xy_in_order = False
#                 yz_in_order = False
#                 # print "xi: {} yj: {}".format(xi, yj)
#                 if xi < yj:
#                     xy_in_order = True
#                 if xy_in_order:
#                     for zk in z_indices:
#                         # print "yj: {} zk: {}".format(yj, zk)
#                         if yj < zk:
#                             # print "break 1: yj < zk"
#                             yz_in_order = True
#                             break
#                 if (xy_in_order and yz_in_order):
#                     # print "break 2: xi < yj"
#                     break
#             if (xy_in_order and yz_in_order):
#                 # print "break 3: for xi"
#                 break
        
#         if not (xy_in_order and yz_in_order):
#             # print "Removing candidate: {}".format(candidate)
#             access_codes.remove(candidate)



#     # for index in meta[str(divisor)]["indices"]
#     # if 
#     # Each number needs to have a divisor that in turn has a divisor in its list
#     # Use divisor as a reference and then check whether there is an option in order
#     return access_codes



# Version with DEBUG Statements above ^

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

        if not is_in_order(x_indices, y_indices, z_indices):
            access_codes.remove(candidate)

    return access_codes

def is_in_order(x_indices, y_indices, z_indices):
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
    return xy_in_order and yz_in_order




def test(l, expected):
    print "solution({})".format(str(l))
    print "************************************************"
    result = solution(l)
    print "************************************************"
    print "expected: {}".format(expected)
    print "result: {}".format(result)
    if result == str(expected):
        print "solution({})".format(str(l))
        print "PASSED"
    else:
        print "solution({})".format(str(l))
        print "FAILED"
    print "\n"

# def test(l, expected):
#     print "solution({})".format(str(l))
#     print "************************************************"
#     solution(l)
#     print "************************************************"

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

print "************************************************"



def make_list(upper_length=2001, upper_int=1000000, fixed=None):
    l = []
    if fixed != None and isinstance(fixed, int):
        for i in range(fixed+1):
            l.append(random.randint(1, upper_int))
        return l
    else:
        for i in range(random.randint(2, upper_length)):
            l.append(random.randint(1, upper_int))
        return l


for test in range(2):
    run_times = []
    list_lengths = []
    # if test == 0:
    #     upper_length = 20
    # else:
    #     upper_length = test * 20 * 5
    for i in range(10):
        # test_list = make_list(upper_length=upper_length)
        test_list = make_list(fixed=2000)
        list_lengths.append(len(test_list))
        run_times.append(timeit.timeit("solution(" + str(test_list) + ")", setup="from __main__ import solution", number=1))

    average_run_time = sum(run_times)/len(run_times)
    average_list_length = sum(list_lengths)/len(list_lengths)
    print "times run: {}".format(len(run_times))
    print "average run time {}".format(average_run_time)
    print "average list length {}".format(average_list_length)

    print "************************************************"