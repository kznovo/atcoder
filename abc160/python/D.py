N, X, Y = [int(i) for i in input().split()]

X -= 1
Y -= 1

a = [0] * N
for i in range(N - 1):
    for j in range(i + 1, N):
        a[min((j-i), abs(i-X)+1+abs(j-Y))] += 1

for k in range(1, N):
    print(a[k])
