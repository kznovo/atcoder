# TODO

from scipy.special import comb

K = int(input())
S = input()

n = len(S)

ans = 0
for i in range(K):
    now = 26 ** (K-i)
    now *= 25 ** i
    now *= comb(i+n-1, n-1, exact=True)
    ans += now

print(ans)
