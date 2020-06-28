from itertools import accumulate

N, M, K = map(int, input().split())
a = [0] + list(accumulate(int(i) for i in input().split()))
b = [0] + list(accumulate(int(i) for i in input().split()))

cnt = 0
best0 = M
for i in range(N+1):
    ai = a[i]
    for j in range(best0, -1, -1):
        bj = b[j]
        if ai + bj <= K:
            cnt = max(cnt, i + j)
            best0 = j
            break

print(cnt)

