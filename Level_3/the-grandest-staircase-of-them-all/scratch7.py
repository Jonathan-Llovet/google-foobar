from itertools import combinations
from collections import deque

def get_candidates(n):
    if n < 3:
        return 0
    nums = list(range(1, n))
    candidates = deque()
    for size in range(1, n):
        candidates.extend(filter(lambda x: sum(x) == n, list(combinations(nums, size))))
    return len(candidates)

for case in range(1,20):
    if case < 3:
        case_candidates = []
    else:
        case_candidates = get_candidates(case)
    print "Calculating for case: {}".format(case)
    print "Number of candidates: {}".format(len(case_candidates))
    print case_candidates
