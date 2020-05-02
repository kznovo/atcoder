A, B, N = [int(i) for i in input().split()]

def f(x: int) -> int:
    return (A * x) // B - A * (x // B)

x = min(N, B - 1)
print(f(x))
