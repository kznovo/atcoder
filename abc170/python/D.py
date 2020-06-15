N = int(input())
A = sorted(int(a) for a in input().split())

# エラトステネスの篩
max_A = A[-1]
search_list = [True for _ in range(max_A)]

count = 0
for i, a in enumerate(A):
    if not search_list[a - 1]:
        continue
    for j in range(a, max_A + 1, a):
        search_list[j - 1] = False
    if i < N - 1 and A[i + 1] == a:
        continue
    count += 1

print(count)
