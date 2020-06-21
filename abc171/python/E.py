N = int(input())
a = [int(i) for i in input().split()]

t = 0
for i in a:
    t ^= i

for i in a:
    print(t ^ i)

