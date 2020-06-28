# TODO
N, P = map(int, input().split())
S = input()

res = 0
for l in range(N):
    for r in range(l+1, N+1):
        sub = int(S[l:r])
        if sub % P == 0:
            res += 1

print(res)

