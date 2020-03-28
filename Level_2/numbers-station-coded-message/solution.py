import timeit

def solution(l, t):
    # Increment end index for each starting index
        # Keep track of intermediate calculations
            # calculated = dict({})
        # What's the best way to keep track of intermediate calculations?
    for start_index in range(len(l)):
        # print "start_index: %d" % start_index
        for end_index in range(start_index, len(l)):
            # print "end_index: %d" % end_index
            #refactor out nested loop if possible
            a = sum_sublist(l, start_index, end_index)
            # print "stats a: %d start_index: %d end_index: %d" % (a, start_index, end_index)
            if a == t:
                return [start_index, end_index]
            if a > t:
                break
    # If sublist cannot be found
    return [-1, -1]

def sum_sublist(l, start, end):
    if start == end:
        return l[start]
    subtotal = 0
    for i in range(start, end+1):
        subtotal += l[i]
    return subtotal

import random
def make_list():
    l = []
    for i in range(random.randint(0,100)):
        l.append(random.randint(0,100))
    return l

run_times = []

for i in range(100000):
    run_times.append(timeit.timeit("solution(" + str(make_list()) + ", " + str(random.randint(0, 250)) + ")", setup="from __main__ import solution, sum_sublist", number=10))

average = sum(run_times)/(10*len(run_times))
print "times run: {}".format(len(run_times))
print "average {}".format(average)