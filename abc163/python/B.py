N, M = [int(i) for i in input().split()]
a_list = [int(i) for i in input().split()]

print(max(N - sum(a_list), -1))
