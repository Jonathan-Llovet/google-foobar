from collections import deque as deque

# for a given int n, what is the maximum sum of all ints in range(1, n+1)?

# for a given remaining_bricks, how many ways are there to combine decreasing integers to equal it?

bricks = 200
options = 0

branch_capacities = dict({})
for num in range(bricks, 1, -1):
    max_sum_branch_children = num * (num + 1) / 2
    # if max_sum_branch_children <= bricks:
    #     break
    branch_capacities.update({str(num): max_sum_branch_children})


def get_children(node, remaining_bricks=None, branch_capacities=branch_capacities, options=options):
    # grandchildren_exist = False
    if remaining_bricks == None:
        remaining_bricks = node
    children_values = []

    for child in range(1, remaining_bricks+1):
        print "handling child: {} with remaining_bricks: {}".format(child, remaining_bricks)
        if child == remaining_bricks:
            options += 1
            print "incrementing options: {}".format(options)
        if child <= 3:
            continue
        if str(child) in branch_capacities.keys():
            # print "retrieving child: {} from branch_capacities: {}".format(child, branch_capacities)
            child_branch_capacity = branch_capacities[str(child)]
            # print "subbranch capacity of {}: {}".format(child, child_branch_capacity)
            # print "subbranch capacity (calculated) of {}: {}".format(child, child * (child + 1) / 2)
        else:
            child_branch_capacity = (child * (child + 1) / 2)

        if child_branch_capacity < remaining_bricks:
            continue

        else:
            print "examining child: {} with remaining_bricks: {}".format(child, remaining_bricks)
            children_values.append((child, remaining_bricks - child))

    return dict({"children_values": children_values, "options": options})


# calculated = dict({})

child_deque = deque()
children = get_children(bricks)
children_values = children["children_values"]
options += children["options"]
child_deque.extend(children_values)

# print child_deque
# print "len(child_deque): {}".format(len(child_deque))

while child_deque:
    print "running through next layer"
    grandchildren_deque = deque()
    for child in child_deque:
        print "child: {}".format(child)
        node = child[0]
        remaining_bricks = child[1]
        # print child
        children = get_children(node, remaining_bricks, options=options)
        children_values = children["children_values"]
        options = children["options"]
        # print children
        grandchildren_deque.extend(children_values)

    child_deque = grandchildren_deque

    # child_deque.extend(get_children(node, remaining_bricks, options=options))
    
    # print "bricks: {} child: {} remaining_bricks: {} grandchildren: {}".format(bricks, child, bricks-child, get_children(child, bricks-child))
    # print "number of grandchildren: {}".format(len(get_children(child, bricks-child)))

# print child_deque
print "len(child_deque): {}".format(len(child_deque))
print "options: {}".format(options)
