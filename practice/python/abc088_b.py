N = int(input())
a = sorted((int(i) for i in input().split()), reverse=True)

alice = 0
bob = 0
for i in range(0, N, 2):
    try:
        alice += a[i]
        bob += a[i+1]
    except:
        pass
print(alice - bob)
