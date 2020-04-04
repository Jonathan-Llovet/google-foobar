def solution(n):
    bricks = n
    max_sum_elements_of_branches = dict({})
    
    def get_viable_children(parent):
        first_child = parent - 1
        smallest_child = 1
        for child in range(first_child, 0, -1):
            if str(child) in max_sum_elements_of_branches.keys():
                continue
            max_sum_branch_children = child * (child + 1) / 2
            if max_sum_branch_children <= n:
                smallest_child = child + 1
                break
            max_sum_elements_of_branches.update({str(child): max_sum_branch_children})
        midway = (first_child + smallest_child) / 2
        branch_children = {
            "first_child": first_child,
            "smallest_child": smallest_child,
            "midway": midway
            }
        return branch_children
    
    tree = get_viable_children(bricks)
    # midway = (len(max_sum_elements_of_branches.keys()) + 1) / 2
    # midway = (first_child + smallest_child) / 2

    print tree

    print "max_sum_elements_of_branches: {}".format(max_sum_elements_of_branches)
    # print "children: {}".format(sorted([int(key) for key in max_sum_elements_of_branches.keys()]))
    print "first_child: {}".format(tree["first_child"])
    # print "first_child: {}".format(first_child)
    print "smallest_child: {}".format(tree["smallest_child"])
    # print "smallest_child: {}".format(smallest_child)
    
    print "midway: {}".format(tree["midway"])
    # print "midway: {}".format(midway)

# for n in range(201):
for n in range(1,21):
    print "solution({})".format(n)
    solution(n)
    print "******************************************"