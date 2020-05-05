A, B, C = [int(i) for i in input().split()]

A, B, C = B, A, C
A, B, C = C, B, A

print("%s %s %s" % (A, B, C))
