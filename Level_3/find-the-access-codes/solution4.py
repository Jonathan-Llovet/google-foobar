def solution(l):
    """Returns the number of access codes that are present in the list l

    The access codes contained in the list l are "lucky triples".
    "Lucky triples" are defined as a tuple (x, y, z) where x divides y and y
    divides z, and where the indices (x_i, y_j, z_k) satisfy i < j < k, such as
    (1, 2, 4).

    Args:
        l: List of integers potentially containing access codes

    Returns:
        An integer indicating how many access codes are present in list l
        If no access codes are found, 0 is returned.
    """
    graph = dict({})

    access_codes = 0

    for i, v in enumerate(list(l[:-1])):
        outbound_connections = []
        for j, w in enumerate(l):
            if j > i and w % v == 0:
                outbound_connections.append(str(j))
        if outbound_connections:
            graph.update({str(i): outbound_connections})

    for node in sorted(graph.keys()):
        connected_nodes = graph[node]
        for connected_node in connected_nodes:            
            access_codes += count_outbound_connections(graph, connected_node)
    return access_codes

def count_outbound_connections(graph, node):
    if node in graph:
        return len(graph[str(node)])
    else:
        return 0
