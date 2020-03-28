# Input:
# solution.solution([13, 5, 6, 2, 5], [5, 2, 5, 13])
# Output:
#     6

# Input:
# solution.solution([14, 27, 1, 4, 2, 50, 3, 1], [2, 4, -4, 3, 1, 1, 14, 27, 50])
# Output:
#     -4

# a = [14, 27, 1, 4, 2, 50, 3, 1]
# b = [2, 4, -4, 3, 1, 1, 14, 27, 50]

# a = [14, 27, 1, 4, 2, 50, 3, 1]
# b = [2, 4, -4, 3, 1, 1, 14, 27, 50]

# c = [13, 5, 6, 2, 5]
# d = [5, 2, 5, 13]


def solution(x, y):
    """Returns ID that is only present in one of the two lists passed as args
    
    Args:
        x: list of prisoner IDs
        y: list of prisoner IDs
    Returns:
        int value of the additional prisoner ID
    """
    try:
        a = set(x)
        b = set(y)
    except TypeError:
        raise TypeError("Args must be lists of IDs")
    c = a.symmetric_difference(b)
    # c is a set containing the ID that is only present in one of the lists
    if len(c) == 0:
        raise ValueError("Args have same set of IDs. " +
                        "One additional ID expected.")
    if len(c) > 1:
        raise ValueError("More than one additional ID " +
                        "found: %s One expected." % list(c))
    return c.pop()


def same_sets():
    print "Running same_sets"
    c = [13, 5, 2]
    d = [5, 2, 5, 13]
    print solution(c, d)

def multiple():
    print "Running multiple"
    c = [13, 5, 2, 5, 6]
    d = [5, 2, 5, 13, 7]
    print solution(c, d)

def run():
    print "Running run"
    c = [13, 5, 6, 2, 5]
    d = [5, 2, 5, 13]
    print solution(c, d)

def bad1():
    print "Running bad1"
    c = 13
    d = [5, 2, 5, 13]
    print solution(c, d)

def bad2():
    print "Running bad2"
    c = 13
    d = [5, 2, 5, 13]
    print solution(c, d)

def bad3():
    print "Running bad3"
    c = 13
    d = 12
    print solution(c, d)

# same_sets()
# multiple()
# run()
# bad1()
# bad2()
# bad3()