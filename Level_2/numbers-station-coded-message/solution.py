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
