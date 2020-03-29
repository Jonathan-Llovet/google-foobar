def solution(xs):
    """Returns integer representing maximum power output of solar panel array

    Args:
        xs: List of integers representing power output of
        each of the solar panels in a given array
    """
    negatives = []
    smallest_negative = None
    positives = []
    contains_panel_with_zero_power = False

    if isinstance(xs, list) and not xs:
        raise IndexError("xs must be a non-empty list. Empty list received.")

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
        # Best-case scenario is zero power output for panel array. Looking bad.
        if contains_panel_with_zero_power:
            max_power = 0
        else:
            # Panel array is draining power. Ouch.
            max_power = negatives.pop()
        return str(max_power)

    # Ensures panels with negative outputs are in pairs to take
    # advantage of the panels' wave stabilizer, which makes paired
    # negative-output panels have a positive output together
    if positives and len(negatives) % 2 != 0:
        negatives.remove(smallest_negative)

    max_power = 1 # initialize for multiplication
    panel_outputs = positives
    panel_outputs.extend(negatives)

    for output in panel_outputs:
        max_power *= output

    return str(max_power)
