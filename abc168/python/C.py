import math

A, B, H, M = (int(i) for i in input().split())

rad = math.pi * 2 * (H / 12 + (M / 60) / 12 - M / 60)

rsq = A**2 + B**2 - 2 * A * B * math.cos(rad)

print(math.sqrt(rsq))

