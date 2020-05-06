K, N = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]

m = K + A[0] - A[-1]
for i in range(len(A) - 1):
    m = max(m, A[i + 1] - A[i])

print(K - m)
