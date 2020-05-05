def fizzbuzz_sum(n: int) -> int:
    return sum(i if i % 3 != 0 and i % 5 != 0 else 0 for i in range(1, n + 1))

N = int(input())
print(fizzbuzz_sum(N))
