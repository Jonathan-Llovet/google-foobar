from itertools import combinations
from collections import deque

def solution(n):
    if n < 3:
        return 0
    nums = list(range(1, n))
    candidates = deque()
    for size in range(1, n):
        candidates.extend(filter(lambda x: sum(x) == n, list(combinations(nums, size))))
    return len(candidates)
