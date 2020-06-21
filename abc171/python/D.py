N = int(input())
A = [int(i) for i in input().split()]
Q = int(input())

sum_A = sum(A)
memo = [0] * 100001
for a in A:
    memo[a] += 1

for _ in range(Q):
    B, C = map(int, input().split())
    sum_A += (C - B) * memo[B]
    memo[C] += memo[B]
    memo[B] = 0
    print(sum_A)

