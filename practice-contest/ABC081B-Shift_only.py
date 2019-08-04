#!/usr/bin/env python3
input()
a = [int(s) for s in input().split(" ")]
r = 0
while all(ia % 2 == 0 for ia in a):
    r += 1
    a = [ia / 2 for ia in a]
print(r)
