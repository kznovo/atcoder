from collections import Counter

S = input()
d = Counter(S)
invert = {v: k for k, v in d.items()}
print(invert[max(invert)])
