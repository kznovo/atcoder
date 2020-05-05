def gcd(i: int, j: int) -> int:
    if j == 0:
        return i
    return gcd(j, i % j)


K = int(input())
res = 0
for a in range(1, K + 1):
    for b in range(1, K + 1):
        gcd_ab = gcd(a, b)
        for c in range(1, K + 1):
            res += gcd(gcd_ab, c)

print(res)
