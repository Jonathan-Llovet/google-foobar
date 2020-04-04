# def solution(n):
#     configurations = traverse_children(n)
#     print "For {} bricks there are {} configurations".format(n, configurations)
#     return configurations

# def traverse_children(parent):
#     configuration_options = 0
    
#     # configuration_options += check_branch(root, root-1)
#     m = 1
#     while m < parent:
#         print "parent: {}".format(parent)
#         print "m: {}".format(m)
#         child = parent - m
#         print "child: {}".format(child)
#         configuration_options += check_branch(child, child-1)
#         print "left check_branch\nIncrementing m"
#         m += 1
#     return configuration_options

# def check_branch(parent, child):
#     print "calling check_branch({}, {})".format(parent, child)
#     if parent == child:
#         print "parent == child: True"
#         print "returning 0"
#         return 0 # may be issue
#     if child <= 1:
#         print "child <= 1"
#         print "child: {}".format(child)
#         print "returning 0"
#         return 1
#     if parent > child:
#         print "parent > child"
#         print "parent: {} child: {}".format(parent, child)
#         difference = child - 1
#         print "difference: {}".format(difference)
#         return check_branch(child, difference)


# def traverse_graph(parent):
    
#     if child < (parent//2) + 1:
#         return 0
    
#     traverse_graph(child, options)
    

#     for n in range(1, (parent//2) + 1):
#         child = parent - n
#         print child
#         if child - n == 1:
#             return 1
#         return options + traverse_graph(child, options)

# traverse_graph(5, options)



# for n in range(1, (parent//2) + 1):
#     print(n)



# def traverse_tree(parent, step):
#     if parent - step == 0:
#         return 0
#     child = parent - step
#     print "parent: {} child: {} step: {}".format(parent, child, step)
#     if child < step:
#         return 1 + traverse_tree(parent, step - 1)
#     return 1
#     # return 1 + traverse_tree(parent, step - 1)

# print solution(3)
# print solution(5)
# print solution(7)
# # print solution(200)


# # def traverse_tree(parent):
# #     for child in range(1, parent):
# #         difference = parent - child
# #         print "parent: {} child: {} difference: {}".format(parent, child, difference)
# #         if parent % 2 == 0: # even
# #             print "parent is even"
# #             if difference < child:
# #                 print "difference < child"
# #                 continue
# #             if difference == child:
# #                 print "difference == child"
# #                 if difference == 1:
# #                     print "difference == 1"
# #                     print "found configuration"
# #                     configurations += 1
# #                     continue
# #                 else:
# #                     traverse_tree(child, configurations)
# #                 # print "found configuration"
# #                 # # traverse_tree(child)
# #                 # configurations += 1
# #                 # print "configurations: {}".format(configurations)
# #                 # return configurations
                
# #         if not parent % 2 == 0: #odd
# #             print "parent is odd"
# #             if difference <= child:
# #                 if difference == 1:
# #                     print "found configuration"
# #                     configurations += 1
# #                     print "configurations: {}".format(configurations)
# #                     return configurations
# #                     print "configurations: {}".format(configurations)
# #                 traverse_tree(child, configurations)
# #         # return configurations + traverse_tree(child)
# #     return configurations


# solution(200)




# def solution(n):
#     root = n
#     children = []
    
#     # def add_children(parent, step):
#     #     child = parent - step
#     #     while child != step:
#     #         children.append(parent-step)
#     #         add_children(parent, step+1)
        

#     for i in range(1,(root//2)+1):
#         children.append(root-i)
    
#     for child in children:
#         for n in range(1,(child//2)+1):
#             children.append(child-n)
#     print children

# solution(7)


def solution(n):
    graph = Graph(n)
    graph.traverse_children(graph.root)
    print "graph leaves: {}".format(graph.leaves)
    print "~~~~~~~~~~GRAPH LEAVES~~~~~~~~~~"
    
class Graph:
    def __init__(self, root):
        self.root = Node(value=root, parent=None, remaining_from_parent=root)
        self.leaves = 0

    def traverse_children(self, node):
        print "current node: {} parent: {}".format(node.value, node.parent)
        if not node.children and node.remaining == 0:
            self.leaves += 1
            print "found leaf: {} parent: {}".format(node.value, node.parent)
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
        print "Finished initializing node. value: {} parent: {} children: {}".format(self.value, self.parent, [child.value for child in self.children])
        print "******************************************************\n"
    def __str__(self):
        return str(self.__dict__)
        # return "Node: value: {} parent: {} children: {}".format(self.value, self.parent, self.children)
    def set_children(self):
        if not self.parent:
            range_bound = (self.value//2) + 1
        else:
            range_bound = self.remaining
        print "setting children for node. value: {} parent: {}".format(self.value, self.parent)
        print "range_bound: {}".format(range_bound)
        for i in range(0, range_bound):
            if self.value == 1:
                print "value == 1; continuing"
                continue
            print "remaining in branch: {}".format(self.remaining) 
            print "i: {}".format(i)
            child_value = self.remaining - i
            print "child_value: {}".format(child_value)
            parent_value = self.value
            remaining = self.remaining
            print "parent_value: {}".format(parent_value)
            if child_value < parent_value:
                if child_value <= self.remaining:
                    print "creating child node. child_value: {}".format(child_value)
                    child = Node(child_value, parent_value, remaining)
                    self.children.append(child)

solution(200)

