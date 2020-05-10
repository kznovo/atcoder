A, B, C, K = [int(i) for i in input().split()]

if K <= A:
    print(K)
elif A + B >= K:
    print(A)
else:
    print(A - (K - (A + B)))
