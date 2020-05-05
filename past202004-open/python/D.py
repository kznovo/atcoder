import re
from itertools import product

S = input()
res = 0
for i in range(1, min(len(S) + 1, 4)):
    for comb in set(product(S + ".", repeat=i)):
        if re.search("".join(comb), S):
            res += 1

print(res)
