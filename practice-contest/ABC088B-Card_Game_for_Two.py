#!/usr/bin/env python3
input()
a = sorted((int(i) for i in input().split(" ")), reverse=True)
l = len(a)
rem = l % 2
r = 0
for i in range(0, l - rem, 2):
    alice = a[i]
    bob = a[i + 1]
    r += alice - bob
if rem:
    r += a[-1]
print(r)
