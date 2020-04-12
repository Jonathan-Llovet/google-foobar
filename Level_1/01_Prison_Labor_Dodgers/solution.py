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
