def main():
    N, K = [int(i) for i in input().split()]
    N = N - (K * (N // K))
    if N == 0:
        print(0)
        return

    prevs = set()
    while N not in prevs:
        prevs.add(N)
        N = abs(N - K)

    print(min(prevs))

main()
