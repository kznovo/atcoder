from collections import defaultdict

N = int(input())
a_dict = defaultdict(int)
for i in input().split():
    a_dict[int(i)] += 1

for i in range(1, N + 1):
    print(a_dict[i])
