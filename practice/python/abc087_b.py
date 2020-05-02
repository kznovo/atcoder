A = int(input())
B = int(input())
C = int(input())
X = int(input())

r = 0
for a in range(A + 1):
    ia = 500 * a
    if ia > X:
        break
    for b in range(B + 1):
        ib = 100 * b
        if ia + ib > X:
            break
        for c in range(C + 1):
            ic = 50 * c
            if ia + ib + ic == X:
                r += 1
print(r)