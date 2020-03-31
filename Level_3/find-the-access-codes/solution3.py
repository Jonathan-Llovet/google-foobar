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

    meta = generate_metadata(l)
    print "final: {}".format(meta)
    access_codes = find_access_codes(meta)
    print access_codes
    return access_codes

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
        # print k_str
        # print meta
    return meta

def calculate_divisors(meta):
    print "in divisor calculation"
    for unique_value in meta.keys():
        print "Outer loop unique_value: {}".format(unique_value)
        k = int(unique_value)
        k_indices = meta[unique_value]["indices"]
        k_divisors = meta[unique_value]["divisors"]
        for divisor_candidate in meta.keys():
            print "divisor_candidate: {}".format(divisor_candidate)
            candidate = int(divisor_candidate)
            if k % candidate == 0:
                print "k mod candidate == 0: {}".format(k % candidate == 0)
                if candidate not in k_divisors:
                    print "Appending candidate: {}".format(candidate)
                    k_divisors.append(candidate)
                    print "k_divisors for {}: {}".format(unique_value, k_divisors)
        meta.update({
                unique_value: {
                    "indices": k_indices,
                    "divisors": k_divisors
                }
            })
    return meta

def generate_metadata(l):
    meta_indices = get_indices(l)
    meta = calculate_divisors(meta_indices)
    return meta


def find_access_codes(meta):
    access_codes = 0
    return str(access_codes)


# def test(l, expected):
#     print "solution({})".format(str(l))
#     print "************************************************"
#     result = solution(l)
#     print "************************************************"
#     print "expected: {}".format(expected)
#     if result == expected:
#         print "solution({})".format(str(l))
#         print "PASSED"
#     else:
#         print "solution({})".format(str(l))
#         print "FAILED"
#     print "\n"

def test(l, expected):
    print "solution({})".format(str(l))
    print "************************************************"
    solution(l)
    print "************************************************"

test([1, 1], 0)
test([1, 1, 2], 1)
# test([1, 1, 1, 1], 1)
test([1, 1, 2, 1, 1], 2)
test([1, 1, 2, 1, 1, 2], 3)
# test([1, 1, 2, 4, 1, 2], 5)
# test([1, 1, 2, 1], 2)
# test([1, 2, 3, 4, 5, 6], 3)
# test([1, 1, 1], 1)
# test([2, 2, 2], 1)
# test([2, 4, 2], 0)
# test([2, 4, 12], 1)
# test([2, 4, 8], 1)
# test([2, 4, 8, 12, 16], 5)
# test([6,5,3,2,1], 0)
# test([], 0)
# test([3,2,5,2,1,6,8],2)
test([31, 31, 1, 4, 2, 62], 2)

# print "************************************************"


"""
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
"""