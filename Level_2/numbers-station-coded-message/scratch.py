l = [4, 3, 10, 2, 8]
t2 = 12

def sum_sublist(l, start, end):
    if start == end:
        return l[start]
    subtotal = 0
    for i in range(start, end):
        subtotal += l[i]
    return subtotal


t = 12
def solution(l, t):
    for i in range(len(l)):
        for j in range(i+1, len(l) + 1):
            a = sum_sublist(l, i, j)
            print "stats a: %d i: %d j: %d" % (a, i, j)
            if a == t:
                print "Found sublist!"
                return [i,j]
            if a > t:
                print "Breaking. Subtotal larger than target %d" % t
                break

print solution(l, t)