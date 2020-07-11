from itertools import combinations_with_replacement
from collections import defaultdict
N = int(input())

def calc(x: int, y: int, z: int) -> int:
    return x**2 + y**2 + z**2 + x*y + y*z + z*x

f = defaultdict(int)
for x,y,z in combinations_with_replacement(range(1, 100), 3):
    l = len(set([x,y,z]))
    num = calc(x,y,z)
    if l == 1:
        f[num] += 1
    elif l == 2:
        f[num] += 3
    else:
        f[num] += 6

for i in range(1, N+1):
    print(f.get(i, 0))

