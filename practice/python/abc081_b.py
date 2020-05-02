n = input()
a = [int(s) for s in input().split()]
i = 0
while all(_a % 2 == 0 for _a in a):
    i += 1
    a = [_a / 2 for _a in a]
print(i)
