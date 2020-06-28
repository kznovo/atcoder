# TODO
from itertools import permutations

N, M = map(int, input().split())


perm = list(permutations(range(1, M+1), N))
res = 0
for A in perm:
    for B in perm:
        for Ai, Bi in zip(A, B):
            if Ai == Bi:
                break
        else:
            res += 1
print(res)
