def solution(n):
    graph = Graph(n)
    graph.traverse_children(graph.root)
    return graph.leaves
    
class Graph:
    def __init__(self, root):
        self.root = Node(value=root, parent=None, remaining_from_parent=root)
        self.leaves = 0

    def traverse_children(self, node):
        if not node.children and node.remaining == 0:
            self.leaves += 1
        for child in node.children:
            self.traverse_children(child)

class Node:
    def __init__(self, value, parent, remaining_from_parent):
        self.value = value
        self.parent = parent
        if not parent:
            self.remaining = value
        else:
            self.remaining = remaining_from_parent - self.value
        self.children = []
        self.set_children()
    def __str__(self):
        return str(self.__dict__)
        # return "Node: value: {} parent: {} children: {}".format(self.value, self.parent, self.children)
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

print solution(9)
# for n in range(1,201):
#     print solution(n)