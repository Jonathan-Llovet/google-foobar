# from itertools import combinations
from collections import deque

# max_sum_elements_of_branches = dict({})
# first_child = parent - 1
# smallest_child = 1
# for child in range(first_child, 0, -1):
#     if str(child) in max_sum_elements_of_branches.keys():
#         continue
#     max_sum_branch_children = child * (child + 1) / 2
#     if max_sum_branch_children <= n:
#         smallest_child = child + 1
#         break
#     max_sum_elements_of_branches.update({str(child): max_sum_branch_children})

# print min(list(map(int, max_sum_elements_of_branches.keys())))


def get_viable_children(parent, max_sum_elements_of_branches):
    print "in get_viable_children"
    print "called with {}".format(parent)
    if not max_sum_elements_of_branches:
        max_sum_elements_of_branches = dict({})
    first_child = parent - 1
    smallest_child = 1

    print "first_child: {}".format(first_child)
    print "smallest_child: {}".format(smallest_child)
    for child in range(parent, -1, -1):
        if str(child) in max_sum_elements_of_branches.keys():
            continue
        max_sum_branch_children = child * (child + 1) / 2
        # if max_sum_branch_children <= parent:
        #     smallest_child = child + 1
        #     break
        max_sum_elements_of_branches.update({str(child): max_sum_branch_children})
    midway = (first_child + smallest_child) / 2
    branch_children = {
        "first_child": first_child,
        "smallest_child": smallest_child,
        "midway": midway
        }
    return branch_children, max_sum_elements_of_branches

viable_combinations = []

def combinations(branch_parent, target, size, branch_capacities):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    # global viable_combinations
    print "inside combinations"
    print "called with branch_parent: {} size: {}".format(branch_parent, size)
    # pool = list(reversed(branch_parent))
    pool = list(branch_parent)
    print "pool: {}".format(pool)
    n = len(pool)
    print "len(pool): {}".format(n)
    if size > n:
        return
    indices = range(size)
    print "indices: {}".format(indices)
    # print "yielding {}".format(list(pool[i] for i in indices))
    if sum(tuple(pool[i] for i in indices)) == target:
        # viable_combinations.extend(tuple(pool[i] for i in indices))
        # print "viable_combinations: {}".format(viable_combinations)
        print "yielding {}".format(tuple(pool[i] for i in indices))
        yield tuple(pool[i] for i in indices)
    loop = 0
    while True:
        loop += 1
        print "loop count: {}".format(loop)
        # print "viable_combinations: {}".format(viable_combinations)
        for i in reversed(range(size)):
        # for i in range(r):
            print "inside range(size): {}".format(list(range(size)))
            # print "inside reversed(range(r)): {}".format(list(reversed(range(r))))
            print "i: {} n: {} r: {}".format(i, n, size)
            print "indices[i]: {}".format(indices[i])
            print "i + n - r: {}".format(i + n - size)
            print ("indices[i] != i + n - r: {}").format(indices[i] != i + n - size)
            if branch_capacities[str(pool[i])] < target:
            # if branch_capacities[str(i)] < target:
                # print "indices[{}] < branch_capacities['{}'] == True".format(i, i)
                print "str(pool[{}]): {}".format(i, str(pool[i]))
                # print "str({}): {}".format(i, str(i))
                # print "branch_capacities[str({})] < {} == True".format(i, target)
                print "branch_capacities[str(pool[{}])] < {} == True".format(i, target)
                # print "branch_capacities[str({})]: {}".format(i, branch_capacities[str(i)])
                print "branch_capacities[str(pool[{}])]: {}".format(i, branch_capacities[str(pool[i])])
                print "returning from function"
                return      
            if indices[i] != i + n - size:
                print "breaking out of loop"
                break
        else:
            print "returning from function"
            return
        indices[i] += 1
        print "incremented indices[i]: {}".format(indices[i])
        print "indices: {}".format(indices)
        print "inside range(i+1, r): {}".format(list(range(i+1, size)))
        print "i+1: {} r: {}".format(i+1, size)
        for j in range(i+1, size):
            print "j: {}".format(j)
            print "updating indices[j]: {}".format(indices[j])
            print "for reference: indices[j-1]: {}".format(indices[j-1])
            print "updating to indices[j-1] + 1: {}".format(indices[j-1] + 1)
            indices[j] = indices[j-1] + 1
            print "after update indices[j]: {}".format(indices[j])
            print "after update indices: {}".format(indices)
        if sum(tuple(pool[i] for i in indices)) == target:
            # viable_combinations.extend(tuple(pool[i] for i in indices))
            # print "viable_combinations: {}".format(viable_combinations)
            print "yielding {}".format(tuple(pool[i] for i in indices))
            yield tuple(pool[i] for i in indices)
    # yield viable_combinations
    # return



def get_candidates(n):
    if n < 3:
        return 0

    branch_capacities = dict({})
    branch_children, branch_capacities = get_viable_children(n, branch_capacities)

    print "branch_children: {}".format(branch_children)
    print "branch_capacities: {}".format(branch_capacities)

    # nums = xrange(1, n)
    nums = range(n-1, 0, -1)
    # global viable_combinations
    # candidates = 0
    candidates = deque()
    for size in xrange(2, n):
        candidates.extend((combinations(nums, n, size, branch_capacities)))
        # candidates.extend(filter(lambda x: sum(x) == n, list(combinations(nums, n, size))))
        # candidates.extend(list(combinations(nums, n, size)))
        # combinations(nums, n, size)
        # candidates.extend(viable_combinations)
        print "candidates for {}: {}".format(n, candidates)
        # print viable_combinations
        # candidates.extend(filter(lambda x: sum(x) == n, list(combinations(nums, size))))
    # return len(candidates)
    return len(candidates)


for case in xrange(3,10):
    print "*********************************************"
    print "Calculating for case: {}".format(case)
    if case < 3:
        case_candidates = 0
    else:
        case_candidates = get_candidates(case)
    # print "Number of candidates: {}".format(len(case_candidates))
    print case_candidates

# 487.067.745