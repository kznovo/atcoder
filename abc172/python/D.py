N = int(input())

res = 0
for i in range(1,N+1):
    y = N // i
    s = y * (y+1) // 2
    res += s * i

print(res)
