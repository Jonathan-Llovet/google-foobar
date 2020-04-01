def solution(l):
    """Returns the number of access codes that are present in the list l

    The access codes contained in the list l are "lucky triples".
    "Lucky triples" are defined as a tuple (x, y, z) where x divides y and y
    divides z, and where the indices (xi, yj, zk) satisfy i < j < k, such as
    (1, 2, 4).

    Args:
        l: List of integers potentially containing access codes

    Returns:
        An integer indicating how many access codes are present in list l
        If no access codes are found, 0 is returned.
    """
    if isinstance(l, list) and not l:
        raise IndexError("l must be a non-empty list. Empty list received.")

    access_codes = 0

    # Transform list into an acyclic directed graph
    graph = dict({})
    for node_index, node_value in enumerate(list(l[:-1])):
        outbounds = find_outbound_connections(l, node_index, node_value)
        if outbounds:
            graph.update({str(node_index): outbounds})

    # find all paths with 2 steps
    for node in sorted(graph.keys()):
        connected_nodes = graph[node]
        for connected_node in connected_nodes:
            access_codes += count_outbound_connections(graph, connected_node)
    return access_codes

def find_outbound_connections(l, node_index, node_value):
    """Returns a list indicating the destination nodes of outbound edges

    Helper function for constructing a graph showing which integers in list l
    are divisors of integers in l with a larger index.

    Args:
        l: The list of integers that contain potential nodes in graph
        node_index: The index of the current node in l
        node_value: The value of the current node in l

    Returns:
        list of integers representing the destination node indices for edges
        outbound from the node represented by node_index and node_value.
    """
    outbound_connections = []
    for destination_index, destination_value in enumerate(l):
        if destination_index > node_index:
            # avoids processing items out of order
            # outbound connections must be to later elements in list
            if destination_value % node_value == 0:
                outbound_connections.append(str(destination_index))
    return outbound_connections

def count_outbound_connections(graph, node):
    if node in graph:
        return len(graph[str(node)])

    return 0
