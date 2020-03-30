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
        return access_codes
    
    calculated = dict({})
    for i in range(len(l)):
        # print i
        if str(l[i]) not in calculated.keys():
            # print "Updating calculated"
            calculated.update({str(l[i]): [i]})
            # print calculated
        else:
            # print "Updating calculated"
            indices = calculated[str(l[i])]
            indices.append(i)
            # print indices
            calculated.update({str(l[i]): indices})
            # print calculated
    
    int_keys = [int(key) for key in calculated.keys()]
    unique_values = sorted(int_keys, reverse=True)

    # print "calculated: {}".format(calculated)
    # print "unique_values: {}".format(unique_values)
    
    secret_key_candidates = []

    for k in unique_values:
        for j in unique_values:
            # if j == 1:
            #     continue
            if k % j == 0:
                i = k / j
                if i in unique_values:
                    candidate = sorted([i, j, k])
                    if candidate not in secret_key_candidates:
                        secret_key_candidates.append(candidate)

    # print "secret_key_candidates: {}".format(secret_key_candidates)

    # iterate over candidates and check indices against calculated

    def verify_secret_key_candidate_positions(secret_key_candidates, indices=(0,1)):
        for candidate in secret_key_candidates:
            i_value = candidate[indices[0]]
            j_value = candidate[indices[1]]
            # k = candidate[2]
            li = calculated[str(i_value)] # list of indices from l
            lj = calculated[str(j_value)]
            # print "li: {}".format(li)
            # print "lj: {}".format(lj)
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
    
    key_candidates = verify_secret_key_candidate_positions(secret_key_candidates, (0,1))
    # print "++++++++++++++++++++++++++++++++++++++++"
    # print "key_candidates: {}".format(key_candidates)
    secret_keys = verify_secret_key_candidate_positions(key_candidates, (1,2))
    # print "++++++++++++++++++++++++++++++++++++++++"
    # print "secret_keys: {}".format(secret_keys)
    access_codes = len(secret_keys)
# calculated: {'1': [0], '3': [2], '2': [1], '5': [4], '4': [3], '6': [5]}
# unique_values: [6, 5, 4, 3, 2, 1]
# secret_key_candidates: [[1, 6, 6], [2, 3, 6], [1, 5, 5], [1, 4, 4], [2, 2, 4], [1, 3, 3], [1, 2, 2]]
# li: [0]
# lj: [5]
    
    # print "secret_key_candidates: {}".format(secret_key_candidates)
    # for candidate in secret_key_candidates:

    # k = len(unique_values) - 1
    # print k
    # print unique_values[k]

    # Naive solution - Times out
    # for i in range(len(l)):
    #     for j in range(i+1, len(l)):
    #         for k in range(j+1, len(l)):
    #             if l[k] % l[j] == 0:
    #                 if l[j] % l[i] == 0:
    #                     # print "values: i: {} j: {} k: {}".format(l[i], l[j], l[k])
    #                     # print "indices: i: {} j: {} k: {}".format(i, j, k)
    #                     access_codes += 1
    # # print access_codes
    return access_codes


# Test Cases
# Input:
print solution([1, 2, 3, 4, 5, 6])
# Output:
#     3

# Input:
print solution([1, 1, 1])
# Output:
#     1

print solution([1, 2, 3, 4, 5, 6, 3, 2, 6, 18, 23, 45, 2])

print "===================================================="

# Max: 2147483647



def make_list():
    l = []
    for i in range(random.randint(2, 2001)):
        l.append(random.randint(1, 1000000))
    return l

run_times = []
list_lengths = []

for i in range(100):
    test_list = str(make_list())
    list_lengths.append(len(test_list))
    run_times.append(timeit.timeit("solution(" + test_list + ")", setup="from __main__ import solution", number=1))

average_run_time = sum(run_times)/len(run_times)
average_list_length = sum(list_lengths)/len(list_lengths)
average_run_time_by_list_length = average_run_time/average_list_length
print "times run: {}".format(len(run_times))
print "average run time {}".format(average_run_time)
print "average list length {}".format(average_list_length)
print "average run time by list length {}".format(average_run_time_by_list_length)

print "************************************************"