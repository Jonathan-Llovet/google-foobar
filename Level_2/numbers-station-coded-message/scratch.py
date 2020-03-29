import timeit

def solution(l, t):
    """ Verifies if substring exists in l containing encoded message with key t

    Args:
        l: A non-empty list of integers potentially containing encoded message
        t: An integer key to check for an encoded message

    Returns:
        A list containing the start and end indices of sublist containing
        encoded message, if one is found. This will be the first instance of a
        sublist that sums to the key t within list l. For example:

        [1, 3]

        If no sublist is found that sums to the key t, then a list is
        returned that indicates no encoded message was found. That list is:

        [-1, -1]

    """
    if isinstance(l, list) and not l:
        raise IndexError("l must be a non-empty list. Empty list received.")

    if not isinstance(l, list) or not isinstance(t, int):
        raise TypeError("Invalid types. Expected list l and int t.\n" +
                        "Received types l: {}, t: {}".format(type(l), type(t)))

    for start_index in range(len(l)):

        subtotal = l[start_index]

        # Check whether single entry equals target
        if subtotal == t:
            return [start_index, start_index]

        # Add successive entries until target found or exceeded
        for end_index in range(start_index + 1, len(l)):
            subtotal += l[end_index]
            if subtotal == t:
                return [start_index, end_index]
            if subtotal > t:
                break

    # Indicate that sublist was not found
    return [-1, -1]


# Solution 1: Imperative sum_sublist
# times run: 100000
# average 5.09376835823e-05

# Solution 2: Functional sum_sublist
# times run: 100000
# average 4.87596058846e-05

# Solution 3: Functional sum_sublist, cache intermediate calculations
# times run: 100000
# average 0.000562442457676

# Solution 4: Semi-functional sum_sublist defined outside solution,
#             cache intermediate calculations
# times run: 100000
# average 0.00121669625998

# Solution 5: Refactored version of solution without sum_sublist function
# times run: 100000
# average 2.51689338684e-05



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
    for i in range(random.randint(1,100)):
        l.append(random.randint(0,100))
    return l

run_times = []

for i in range(100000):
    run_times.append(timeit.timeit("solution(" + str(make_list()) + ", " + str(random.randint(0, 250)) + ")", setup="from __main__ import solution", number=1))

average = sum(run_times)/len(run_times)
print "times run: {}".format(len(run_times))
print "average {}".format(average)


