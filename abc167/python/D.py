# TODO
N, K = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]


city = 1
prevs = []
for _ in range(K):
    city = A[city - 1]
    if city in prevs:
        rem = prevs.index(city)
        loop = len(prevs[rem:])
        break
    prevs.append(city)

ix = (K - rem) % loop
print(prevs[rem:][ix - 1])
