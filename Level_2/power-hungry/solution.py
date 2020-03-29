def solution(xs):
    """Finds maximum power output of solar panel array

    Args:
        ...
    Returns:
        ...
    """
    negatives = []
    smallest_negative = None
    positives = []
    contains_panel_with_zero_power = False

    for x in xs:
        if x > 0:
            positives.append(x)
        if x < 0:
            if not smallest_negative or abs(smallest_negative) > abs(x):
                smallest_negative = x
            negatives.append(x)
        if x == 0:
            contains_panel_with_zero_power = True

    if not positives and len(negatives) == 1:
        if contains_panel_with_zero_power:
            max_power = 0
        else:
            max_power = smallest_negative
        return str(max_power)

    if positives and len(negatives) % 2 != 0:
        negatives.remove(smallest_negative)

    max_power = 1 # initialize (multiplicative identity constant)
    positives.extend(negatives)
    panel_outputs = positives
    for output in panel_outputs:
        max_power *= output
    return str(max_power)
