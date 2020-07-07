# TODO
N, K = map(int, input().split())
A = sorted(map(int, input().split()))
mod = 10 ** 9 + 7

calc = []
for k in range(K - (K%2)):
    if abs(A[0]) > abs(A[-1]):
        calc.append(A[0])
        del A[0]
    else:
        calc.append(A.pop())

res = 1
for c in calc:
    res *= c
if K%2:


abs_A = sorted(abs(a) for a in A, reverse=True)
calc = abc_A[:K-(K%2)]
for k in range(K - (K % 2)):



if K % 2 == 0:
    res_1 = 1
    for a in A[-K:]:
        res_1 *= a
    res_2 = 1
    for a in A[:K]:
        res_2 *= a
    res = max(res_1, res_2)
    print(res % mod)
else:
    A =
