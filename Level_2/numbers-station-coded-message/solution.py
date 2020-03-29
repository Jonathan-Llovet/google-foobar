def solution(l, t):
    """ Verifies if substring exists in l containing encoded message with key t

    Args:
        l: A list of integers potentially containing encoded message in sublist
        t: An integer key to check for an encoded message

    Returns:
        A list containing the start and end indices of sublist containing
        encoded message, if one is found. This will be the first instance of a
        sublist that sums to the key t within list l. For example:

        [1, 3]

        If no sublist is found that sums to the key t, then a list is
        returned that indicates no encoded message was found. That list is:

        [-1, -1]
        
    Raises:
        ...

    """
    for start_index in range(len(l)):
        subtotal = l[start_index]
        # Case where single entry equals target
        if subtotal == t:
            return [start_index, start_index]
        for end_index in range(start_index + 1, len(l)):
            # Add each successive entry until target found or exceeded
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
