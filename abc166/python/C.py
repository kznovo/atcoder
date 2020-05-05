N, M = [int(i) for i in input().split()]
H = {i: int(h) for i, h in enumerate(input().split(), 1)}
t = {k: 0 for k in H.keys()}

for _ in range(M):
    A, B = [int(i) for i in input().split()]
    t[A] = max(H[B], t[A])
    t[B] = max(H[A], t[B])

print(sum(H[k] > v for k, v in t.items()))
