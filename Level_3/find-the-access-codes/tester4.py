# def solution(l):
#     """Returns the number of access codes that are present in the list l

#     The access codes contained in the list l are "lucky triples".
#     "Lucky triples" are defined as a tuple (x, y, z) where x divides y and y
#     divides z, and where the indices (x_i, y_j, z_k) satisfy i < j < k, such as
#     (1, 2, 4).

#     Args:
#         l: List of integers potentially containing access codes

#     Returns:
#         An integer indicating how many access codes are present in list l
#         If no access codes are found, 0 is returned.
#     """
#     graph = dict({})

#     access_codes = 0

#     print "constructing graph..."

#     for i, v in enumerate(list(l[:-1])):
#         print "Finding outbound connections for {} in position {}".format(v, i)
#         outbound_connections = []
#         for j, w in enumerate(l):
#             print "examining i: {} j: {} v: {} w: {}".format(i,j,v,w)
#             if j > i and w % v == 0:
#                 print "w % v: {} % {} == {}".format(w, v, (w % v))
#                 outbound_connections.append(str(j))
#                 print "outbound_connections for {}: {}".format(i, outbound_connections)
#         if outbound_connections:
#             graph.update({str(i): outbound_connections})

    
#     print "******"
#     print "constructed graph: {}".format(graph)
#     print "******"
#     print "sorted keys for graph: {}".format(sorted(graph.keys()))
#     print "******"

#     for node in sorted(graph.keys()):
#         connected_nodes = graph[node]
#         print "connected_nodes for node {}: {}".format(node, connected_nodes)
#         for connected_node in connected_nodes:
#             # print ""
            
#             access_codes += count_outbound_connections(graph, connected_node)
    
#     return access_codes

# def count_outbound_connections(graph, node):
#     print "in count_outbound_connections"
#     print "searching for node {} in graph".format(node)
#     if node in graph:
#         print "node found"
#         print "counting outbound connections for node: {}".format(node)
#         print "number of outbound connections: {}".format(len(graph[str(node)]))
#         return len(graph[str(node)])
#     else:
#         print "node not found"
#         print "number of outbound connections: 0"
#         return 0


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


# def test(l, expected):
#     print "solution({})".format(str(l))
#     print "************************************************"
#     result = solution(l)
#     print "************************************************"
#     print "expected: {}".format(expected)
#     print "result: {}".format(result)
#     if result == expected:
#         print "solution({})".format(str(l))
#         print "PASSED"
#     else:
#         print "solution({})".format(str(l))
#         print "FAILED"
#     print "\n"

# test([1, 2, 3, 4, 5, 6], 3)
# test([1, 1, 1], 1)
# test([1, 2, 3], 0)
# test([1, 2], 0)
# test([5, 5, 5], 1)

import random
import timeit

def make_list(upper_length=2001, upper_int=1000000, fixed=None):
    l = []
    if fixed != None and isinstance(fixed, int):
        for i in range(fixed+1):
            l.append(random.randint(1, upper_int))
        return l
    else:
        for i in range(random.randint(2, upper_length)):
            l.append(random.randint(1, upper_int))
        return l


for test in range(2):
    run_times = []
    list_lengths = []
    # if test == 0:
    #     upper_length = 20
    # else:
    #     upper_length = test * 20 * 5
    for i in range(10):
        # test_list = make_list(upper_length=upper_length)
        test_list = make_list(fixed=2000)
        list_lengths.append(len(test_list))
        run_times.append(timeit.timeit("solution(" + str(test_list) + ")", setup="from __main__ import solution", number=1))

    average_run_time = sum(run_times)/len(run_times)
    average_list_length = sum(list_lengths)/len(list_lengths)
    print "times run: {}".format(len(run_times))
    print "average run time {}".format(average_run_time)
    print "average list length {}".format(average_list_length)

    print "************************************************"