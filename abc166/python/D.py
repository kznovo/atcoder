X = int(input())

def f():
    for A in range(-118, 120):
        for B in range(-119, 119):
            if pow(A, 5) - pow(B, 5) == X:
                print(f"{A} {B}")
                return

f()
