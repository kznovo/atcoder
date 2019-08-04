#!/usr/bin/env python3
N, A, B = input().split(" ")
r = sum(i if int(A) <= sum(int(n) for n in str(i)) <= int(B) else 0 for i in range(1, int(N) + 1))
print(r)
