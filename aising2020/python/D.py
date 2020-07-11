from copy import deepcopy

N = int(input())
X = input()


def popcount(n: int) -> int:
    return bin(n)[2:].count("1")


def f(n: int) -> int:
    i = 0
    while n > 0:
        n = n % popcount(n)
        i += 1
    return i


for i in range(N):
    rev = "0" if X[i] == "1" else "1"
    _X = X[:i] + rev + X[i+1:]
    n = int(_X, 2)
    print(f(n))

