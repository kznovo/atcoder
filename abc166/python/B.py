N, K = [int(i) for i in input().split()]
nusuke = set(range(1, N + 1))
nusuke_with_treats = set()

for _ in range(K):
    input()
    for i in input().split():
        nusuke_with_treats.add(int(i))

print(len(nusuke - nusuke_with_treats))
