def solution(l, t):
    # Increment end index for each starting index
        # Keep track of intermediate calculations
            # calculated = dict({})
        # What's the best way to keep track of intermediate calculations?
    for start_index in range(len(l)):
        # TODO: refactor out nested loop if possible
        for end_index in range(start_index, len(l)):
            subtotal = sum_sublist(l, start_index, end_index)
            if subtotal == t:
                return [start_index, end_index]
            if subtotal > t:
                break
    # Sublist was not found
    return [-1, -1]

def sum_sublist(l, start, end):
    if start == end:
        return l[start]
    subtotal = 0
    for i in range(start, end+1):
        subtotal += l[i]
    return subtotal