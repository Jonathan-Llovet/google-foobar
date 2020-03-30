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
    
    meta = dict({})

    for k in range(len(l)):
        k_str = str(l[k])
        if k_str not in meta.keys():
            meta.update({
                k_str: {
                    "indices": [k],
                    "divisors": []
                }
            })
        elif k_str in meta.keys():
            k_indices = meta[k_str]["indices"]
            k_indices.append(k)
            k_divisors = meta[k_str]["divisors"]
            
            
            meta.update({
                k_str: {
                    "indices": k_indices,
                    "divisors": k_divisors
                }
            })
        # print k_str
        # print meta

    for unique_value in meta.keys():
        k = int(unique_value)
        k_indices = meta[unique_value]["indices"]
        k_divisors = meta[unique_value]["divisors"]
        for key in meta.keys():
            divisor_candidate = int(key)
            if k % divisor_candidate == 0:
                if divisor_candidate not in k_divisors:
                    k_divisors.append(divisor_candidate)
        meta.update({
                k_str: {
                    "indices": k_indices,
                    "divisors": k_divisors
                }
            })

    print "final"
    print meta


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

# def test(l, expected):
#     print "solution({})".format(str(l))
#     print "************************************************"
#     solution(l)
#     print "************************************************"

# test([1, 1], 0)
# test([1, 1, 2], 1)
# test([1, 1, 1, 1], 1)
# test([1, 1, 2, 1, 1], 2)
# test([1, 1, 2, 1, 1, 2], 3)
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
# test([31, 31, 1, 4, 2, 62], 2)

# print "************************************************"

def make_list():
    l = []
    for i in range(random.randint(2, 2001)):
        l.append(random.randint(1, 1000000))
    return l

run_times = []
list_lengths = []

for i in range(10):
    test_list = str(make_list())
    list_lengths.append(len(test_list))
    run_times.append(timeit.timeit("solution(" + test_list + ")", setup="from __main__ import solution", number=1))

average_run_time = sum(run_times)/len(run_times)
average_list_length = sum(list_lengths)/len(list_lengths)
print "times run: {}".format(len(run_times))
print "average run time {}".format(average_run_time)
print "average list length {}".format(average_list_length)

print "************************************************"