import math

A, B = map(int, input().split())

res = -1
p = int(B/0.1)

for i in range(p, p+10):
    if math.floor(i*0.08) == A:
        res = i
        break

print(res)

