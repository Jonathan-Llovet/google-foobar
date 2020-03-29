import timeit

def solution(l, t):
    for start_index in range(len(l)):
        subtotal = l[start_index]
        if subtotal == t:
            return [start_index, start_index]
        for end_index in range(start_index + 1, len(l)):
            subtotal += l[end_index]
            if subtotal == t:
                return [start_index, end_index]
            if subtotal > t:
                break
    # Sublist was not found
    return [-1, -1]


# def sum_sublist(l, start, end):
#     if start == end:
#         return l[start]
#     if start < end:
#         return l[start] + sum_sublist(l, (start + 1), end)

# def solution(l, t):
#     # Increment end index for each starting index
#         # Keep track of intermediate calculations
#             # calculated = dict({})
#         # What's the best way to keep track of intermediate calculations?
#     for start_index in range(len(l)):
#         # TODO: refactor out nested loop if possible
#         for end_index in range(start_index, len(l)):
#             # print calculated
#             if str([start_index, end_index]) in calculated.keys():
#                 subtotal = calculated[str([start_index, end_index])]
#                 # print "Got subtotal from cache"
#                 # print "stats subtotal: %d start_index: %d end_index: %d" % (subtotal, start_index, end_index)
#             else:
#                 subtotal = sum_sublist(l, start_index, end_index)
#                 # print "Calculated subtotal"
#                 # print "stats subtotal: %d start_index: %d end_index: %d" % (subtotal, start_index, end_index)
#             if subtotal == t:
#                 return [start_index, end_index]
#             if subtotal > t:
#                 break
#     # Sublist was not found
#     return [-1, -1]

# def sum_sublist(l, start, end):
#     if start == end:
#         return l[start]
#     if start < end:
#         calculated.update({str([(start + 1), end]): sum_sublist(l, (start + 1), end)})
#         return l[start] + sum_sublist(l, (start + 1), end)

# calculated = dict({})
# def sum_sublist(l, calculated_sublists, start, end):
#     if start == end:
#         return l[start]
#     if start < end:
#         return l[start] + sum_sublist(l, calculated, (start + 1), end)

# def sum_sublist(l, start, end):
#     if start == end:
#         return l[start]
#     subtotal = 0
#     for i in range(start, end+1):
#         subtotal += l[i]
#     return subtotal


# Solution 1: Imperative
# times run: 100000
# average 5.09376835823e-05

# Solution 2: Functional
# times run: 100000
# average 4.87596058846e-05


import random
def make_list():
    l = []
    for i in range(random.randint(0,100)):
        l.append(random.randint(0,100))
    return l

run_times = []

for i in range(100000):
    run_times.append(timeit.timeit("solution(" + str(make_list()) + ", " + str(random.randint(0, 250)) + ")", setup="from __main__ import solution", number=1))

average = sum(run_times)/len(run_times)
print "times run: {}".format(len(run_times))
print "average {}".format(average)


