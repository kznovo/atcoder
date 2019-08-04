#!/usr/bin/env python3

def f(n, y):
    if 10000 * n < y:
        print("-1 -1 -1")
        return

    for a in range(n + 1):
        ap = 10000 * a
        max_b = 5000 * (n - a)

        if ap > y:
            break

        if (ap + max_b) < y:
            continue

        for b in range(n + 1 - a):
            bp = 5000 * b

            if (ap + bp) > y:
                break

            c = n - a - b
            cp = 1000 * c
            tmp = ap + bp + cp

            if tmp > y:
                break
            elif tmp == y:
                print("{} {} {}".format(a, b, c))
                return

    print("-1 -1 -1")


N, Y = input().split(" ")
f(int(N), int(Y))
