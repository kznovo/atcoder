# TODO

import numpy as np


N = int(input())
A = np.array([int(i) for i in input().split()])
Q = int(input())
B, C = [], []
for _ in range(Q):
    b, c = map(int, input().split())
    B.append(b)
    C.append(c)

for b, c in zip(B, C):
    A = np.where(A==b, c, A)
    print(A.sum())

