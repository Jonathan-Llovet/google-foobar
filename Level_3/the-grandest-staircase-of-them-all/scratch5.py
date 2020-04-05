"""
from collections import deque as deque

print "\n"*20

bricks = 10
calculated = dict({})

max_sum_elements_of_branches = dict({})
for num in range(1, bricks + 1):
    max_sum_branch_children = child * (child + 1) / 2
    if max_sum_branch_children <= n:
        break
    max_sum_elements_of_branches.update({str(child): max_sum_branch_children})


# if str(child) in max_sum_elements_of_branches.keys():
#     child_branch_max_sum = max_sum_elements_of_branches[str(child)]
#     continue

# for a given int n, what is the maximum sum of all ints in range(1, n+1)?

# for a given remaining_bricks, how many ways are there to combine decreasing integers to equal it?
child_deque = []

def get_children(node, remaining_bricks=None, branch_capacity=max_sum_elements_of_branches):
    grandchildren_exist = False
    if remaining_bricks == None:
        remaining_bricks = node
    children_values = []
    for child in range(1, remaining_bricks):
        # if child < 3:
        #     options += 1
        #     continue
        if str(child) in branch_capacity.keys():
            child_branch_capacity = branch_capacity[str(child)]
        else:
            child_branch_capacity = (child * (child + 1) / 2)
        if child_branch_capacity < remaining_bricks:
            continue
        else:
            print "examining child: {} with remaining_bricks: {}".format(child, remaining_bricks)
            children_values.append((child, remaining_bricks-child))
    return children_values

child_deque.extend(get_children(bricks))

# print child_deque
print "len(child_deque): {}".format(len(child_deque))

options = 0

# print children

print "running through next layer"
for child in child_deque:
    node = child[0]
    remaining_bricks = child[1]
    # print child
    child_deque.extend(get_children(node, remaining_bricks))
    
    # print "bricks: {} child: {} remaining_bricks: {} grandchildren: {}".format(bricks, child, bricks-child, get_children(child, bricks-child))
    # print "number of grandchildren: {}".format(len(get_children(child, bricks-child)))

# print child_deque
print "len(child_deque): {}".format(len(child_deque))
"""



from collections import deque as deque

# print "\n"*20

bricks = 10
calculated = dict({})

max_sum_elements_of_branches = dict({})
for num in range(bricks, 1, -1):
    max_sum_branch_children = num * (num + 1) / 2
    if max_sum_branch_children <= bricks:
        break
    max_sum_elements_of_branches.update({str(num): max_sum_branch_children})


# if str(child) in max_sum_elements_of_branches.keys():
#     child_branch_max_sum = max_sum_elements_of_branches[str(child)]
#     continue

# for a given int n, what is the maximum sum of all ints in range(1, n+1)?

# for a given remaining_bricks, how many ways are there to combine decreasing integers to equal it?
child_deque = []
options = 0

def get_children(node, remaining_bricks=None, branch_capacity=max_sum_elements_of_branches, options=options):
    # print "node: {}".format(node)
    # print "remaining_bricks: {}".format(remaining_bricks)
    # print "branch_capacity: {}".format(branch_capacity)
    # print "options: {}".format(options)
    # grandchildren_exist = False
    if remaining_bricks == None:
        remaining_bricks = node
    children_values = []

    for child in range(1, remaining_bricks):
        if child < 3:
            print "handling child: {} with remaining_bricks: {}".format(child, remaining_bricks)
            options += 1
            print "incrementing options: {}".format(options)
            continue

        if str(child) in branch_capacity.keys():
            print "retrieving child: {} from branch_capacity: {}".format(child, branch_capacity)
            child_branch_capacity = branch_capacity[str(child)]
        else:
            child_branch_capacity = (child * (child + 1) / 2)

        if child_branch_capacity < remaining_bricks:
            continue

        else:
            print "examining child: {} with remaining_bricks: {}".format(child, remaining_bricks)
            children_values.append((child, remaining_bricks - child))
    return dict({"children_values": children_values, "options": options})

children = get_children(bricks)
children_values = children["children_values"]
options += children["options"]


# print children
child_deque.extend(children_values)

print child_deque
print "len(child_deque): {}".format(len(child_deque))

# print children

print "running through next layer"
for child in child_deque:
    print "child: {}".format(child)
    node = child[0]
    remaining_bricks = child[1]
    # print child
    children = get_children(node, remaining_bricks, options=options)
    children_values = children["children_values"]
    options += children["options"]
    # print children
    child_deque.extend(children_values)
    # child_deque.extend(get_children(node, remaining_bricks, options=options))
    
    # print "bricks: {} child: {} remaining_bricks: {} grandchildren: {}".format(bricks, child, bricks-child, get_children(child, bricks-child))
    # print "number of grandchildren: {}".format(len(get_children(child, bricks-child)))

# print child_deque
print "len(child_deque): {}".format(len(child_deque))
