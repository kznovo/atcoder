N = int(input())
A = list(map(int, input().split()))
res = 0
for i in range(0, len(A), 2):
    res += A[i] % 2
print(res)
