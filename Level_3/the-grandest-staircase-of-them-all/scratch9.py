from collections import deque

def get_viable_children(parent, max_sum_elements_of_branches):
    if not max_sum_elements_of_branches:
        max_sum_elements_of_branches = dict({})
    first_child = parent - 1
    smallest_child = 1

    for child in range(parent, -1, -1):
        if str(child) in max_sum_elements_of_branches.keys():
            continue
        max_sum_branch_children = child * (child + 1) / 2
        max_sum_elements_of_branches.update({str(child): max_sum_branch_children})
    midway = (first_child + smallest_child) / 2
    branch_children = {
        "first_child": first_child,
        "smallest_child": smallest_child,
        "midway": midway
        }
    return branch_children, max_sum_elements_of_branches

def combinations(branch_parent, target, size, branch_children, branch_capacities):
    pool = list(branch_parent)
    n = len(pool)
    if size > n:
        return
    indices = range(size)
    if sum(tuple(pool[i] for i in indices)) == target:
        yield tuple(pool[i] for i in indices)
    loop = 0
    while True:
        loop += 1
        for i in reversed(range(size)):
            if pool[i] < branch_children["smallest_child"]:
                return
            if branch_capacities[str(pool[i])] < target:
                return
            if indices[i] != i + n - size:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, size):
            indices[j] = indices[j-1] + 1
        if sum(tuple(pool[i] for i in indices)) == target:
            yield tuple(pool[i] for i in indices)

def solution(n):
    if n < 3:
        return 0
    branch_capacities = dict({})
    branch_children, branch_capacities = get_viable_children(n, branch_capacities)
    nums = range(n-1, 0, -1)
    candidates = deque()
    for size in xrange(2, n):
        candidates.extend((combinations(nums, n, size, branch_children, branch_capacities)))
    return len(candidates)



for case in xrange(3,25):
    if case < 3:
        case_candidates = 0
    else:
        case_candidates = solution(case)
    print "*********************************************"
    print "Calculating for case: {}".format(case)
    print "Number of candidates: {}".format(case_candidates)
    print case_candidates
