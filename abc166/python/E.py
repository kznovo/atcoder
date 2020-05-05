from collections import Counter

N = int(input())
A = [int(height) for height in input().split()]

m = Counter(i - elem for i, elem in enumerate(A))
res = 0
for i, elem in enumerate(A):
    res += m[i + elem]

print(res)
