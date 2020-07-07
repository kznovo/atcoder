# TODO
N = int(input())
A = sorted(map(int, input().split()), reverse=True)
res = 0
min_f = A[0]
for a in A[1:]:
    res += min_f
    min_f = a
print(res)

