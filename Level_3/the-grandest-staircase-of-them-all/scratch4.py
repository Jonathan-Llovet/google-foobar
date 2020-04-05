def solution(n):
    bricks = n
    viable = get_viable_configurations(bricks)
    options = Graph(viable["midway"])
    print viable
    print options
    # viable_configurations = get_viable_configurations(bricks)
    # midway = (len(max_sums_of_branch_elements.keys()) + 1) / 2
    # midway = (largest_child + smallest_child) / 2

max_sums_of_branch_elements = dict({})

# def solution(n):
    # graph = Graph(n)
    # graph.traverse_children(graph.root)
    # return graph.leaves

class Graph:
    def __init__(self, bricks):
        self.size = 0
        self.bricks = bricks
        self.root = Node(bricks)
        # self.root = Node(value=root, parent=None, remaining_from_parent=root)
        # self.leaves = 0
    def add_node(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.root.add_child(value, self.root)
        self.size += 1



    # def traverse_children(self, node):
    #     if not node.children and node.remaining == 0:
    #         self.leaves += 1
    #     for child in node.children:
    #         self.traverse_children(child)


class Node:
    def __init__(self, value, parent=None):
        self.value = value
        if parent != None:
            self.parent = parent.value
        else:
            self.parent = parent
        self.left = None
        self.right = None

    def add_child(self, value, parent):
        options = get_viable_configurations(value)
        if value > parent.value:
            # Go to the right
            if parent.right == None:
                parent.right = Node(value, parent)
                return
            return add_child(value, parent.right)
        else:
            # Go to the left
            if parent.value > options["largest_child"]:
                return
            if parent.left == None:
                parent.left = Node(value, parent)
                return
            return add_child(value, parent.left)

    def get_viable_configurations(self, parent):
        if parent == None:
            branch_children = {
                "largest_child": None,
                "smallest_child": None,
                "midway": None
            }
            # Possibly throw an error
            return branch_children
        largest_child = parent.value - 1
        smallest_child = 1
        for child in range(largest_child, 0, -1):
            max_sum_branch_children = child * (child + 1) / 2
            if max_sum_branch_children <= parent.value:
                smallest_child = child + 1
                break
            if str(child) in max_sums_of_branch_elements.keys():
                continue
            max_sums_of_branch_elements.update({str(child): max_sum_branch_children})
        midway = (largest_child + smallest_child) / 2
        branch_children = {
            "largest_child": largest_child,
            "smallest_child": smallest_child,
            "midway": midway
            }
        return branch_children

# class Node:
#     def __init__(self, value, parent, is_left):
#         self.value = value
#         get_viable_configurations(value)
#         self.parent = parent
#         if not parent:
#             self.remaining = value
#         else:
#             self.remaining = remaining_from_parent - self.value
#         self.children = []
#         self.set_children()
#     def __str__(self):
#         return str(self.__dict__)
#         # return "Node: value: {} parent: {} children: {}".format(self.value, self.parent, self.children)
"""    
    def get_viable_configurations(parent):
        largest_child = parent - 1
        smallest_child = 1
        for child in range(largest_child, 0, -1):
            max_sum_branch_children = child * (child + 1) / 2
            if max_sum_branch_children <= parent:
                smallest_child = child + 1
                break
            if str(child) in max_sums_of_branch_elements.keys():
                continue
            max_sums_of_branch_elements.update({str(child): max_sum_branch_children})
        midway = (largest_child + smallest_child) / 2
        branch_children = {
            "largest_child": largest_child,
            "smallest_child": smallest_child,
            "midway": midway
            }
        return branch_children
    
    
    
    
    
    def set_children(self):
        if not self.parent:
            range_bound = (self.value//2) + 1
        else:
            range_bound = self.remaining
        for i in range(0, range_bound):
            if self.value == 1:
                continue
            child_value = self.remaining - i
            parent_value = self.value
            remaining = self.remaining
            # if remaining - child_value > child_value:
            #     continue
            if child_value < parent_value:
                if child_value <= self.remaining:
                    child = Node(child_value, parent_value, remaining)
                    self.children.append(child)

"""














    # print tree
"""
    print "max_sums_of_branch_elements: {}".format(max_sums_of_branch_elements)
    # print "children: {}".format(sorted([int(key) for key in max_sums_of_branch_elements.keys()]))
    print "largest_child: {}".format(tree["largest_child"])
    # print "largest_child: {}".format(largest_child)
    print "smallest_child: {}".format(tree["smallest_child"])
    # print "smallest_child: {}".format(smallest_child)
    
    print "midway: {}".format(tree["midway"])
    # print "midway: {}".format(midway)
"""
# for n in range(201):
for n in range(1,21):
    print "solution({})".format(n)
    solution(n)
    print "******************************************"