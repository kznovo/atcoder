N, M = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]

lower_lim = sum(A) * (1 / (4 * M))

if any(s < lower_lim for s in sorted(A, reverse=True)[:M]):
    print("No")
else:
    print("Yes")
