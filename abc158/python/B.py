N, A, B = map(int, input().split())

div, mod = divmod(N, (A + B))
res = A * div + min(A, mod)
print(res)

