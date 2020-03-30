import timeit
import random
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
        print "returning access_codes: {}".format(access_codes)
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
    print "calculated: {}".format(str(calculated))
    print "unique_values: {}".format(str(unique_values))
    for k in unique_values:
        print "k: {}".format(str(k))
        for j in unique_values:
            print "j: {}".format(str(j))
            print "k % j: {}".format(str(k % j))
            if k % j == 0:
                if j == 1:
                    i = k
                else:
                    i = k / j
                print "i: {}".format(str(i))
                if i in unique_values:
                    candidate = sorted([i, j, k])
                    print "candidate: {}".format(str(candidate))
                    if candidate not in secret_key_candidates:
                        print "Appending candidate to secret_key_candidates."
                        secret_key_candidates.append(candidate)
                        print "secret_key_candidates: {}".format(str(secret_key_candidates))
    # iterate over candidates and check indices against calculated
    key_candidates = verify_secret_key_candidate_positions(secret_key_candidates, calculated, (0,1))
    secret_keys = verify_secret_key_candidate_positions(key_candidates, calculated, (1,2))
    access_codes = len(secret_keys)
    print "returning access_codes: {}".format(access_codes)
    return access_codes

def verify_secret_key_candidate_positions(secret_key_candidates, calculated, indices=(0,1)):
    print "In verify_secret_key_candidate_positions"
    print "Called for positions {}".format(indices)
    for candidate in secret_key_candidates:
        keep_candidate = None
        if candidate[0] == 1 and candidate[1] == candidate[2]:
            # keep_candidate = True
            continue
        print "candidate: {}".format(candidate)
        i_value = candidate[indices[0]]
        print "i_value: {}".format(i_value)
        j_value = candidate[indices[1]]
        print "j_value: {}".format(j_value)
        li = calculated[str(i_value)] # list of indices from l
        print "li: {}".format(li)
        lj = calculated[str(j_value)]
        print "lj: {}".format(lj)
        for i_index in li:
            print "starting check for i_index: {}".format(i_index)
            for j_index in lj:
                print "i_index: {}".format(i_index)
                print "j_index: {}".format(j_index)
                if i_index < j_index:
                    keep_candidate = True
                    print "keep_candidate: {}".format(keep_candidate)
                    break
            print "Finished checking j_indices for i_index: {}".format(i_index)
            if keep_candidate:
                print "keeping candidate"
                break
            else:
                print "removing candidate"
                secret_key_candidates.remove(candidate)
    print "End verify_secret_key_candidate_positions"
    print "Returning: {}".format(secret_key_candidates)
    print "**********"
    return secret_key_candidates

def test(l, expected):
    print "solution({})".format(str(l))
    print "************************************************"
    result = solution(l)
    print "************************************************"
    print "expected: {}".format(expected)
    if result == expected:
        print "PASSED"
    else:
        print "FAILED"
    print "\n"


test([1, 1], 0)
test([1, 1, 2], 1)
test([1, 1, 2, 1], 2)
test([1, 2, 3, 4, 5, 6], 3)
test([1, 1, 1], 1)


# print solution([1, 2, 3, 4, 5, 6, 3, 2, 6, 18, 23, 45, 2])

# print "************************************************"

# def make_list():
#     l = []
#     for i in range(random.randint(2, 2001)):
#         l.append(random.randint(1, 1000000))
#     return l

# run_times = []
# list_lengths = []

# for i in range(100):
#     test_list = str(make_list())
#     list_lengths.append(len(test_list))
#     run_times.append(timeit.timeit("solution(" + test_list + ")", setup="from __main__ import solution", number=1))

# average_run_time = sum(run_times)/len(run_times)
# average_list_length = sum(list_lengths)/len(list_lengths)
# average_run_time_by_list_length = average_run_time/average_list_length
# print "times run: {}".format(len(run_times))
# print "average run time {}".format(average_run_time)
# print "average list length {}".format(average_list_length)
# print "average run time by list length {}".format(average_run_time_by_list_length)

# print "************************************************"