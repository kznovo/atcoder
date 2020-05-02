N, A, B = [int(i) for i in input().split()]
r = 0
for n in range(1, N + 1):
    _n = sum(int(i) for i in str(n))
    if A <= _n <= B:
        r += n
print(r)
