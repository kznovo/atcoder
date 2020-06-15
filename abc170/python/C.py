def main():
    X, N = map(int, input().split())
    p = list(map(int, input().split()))

    if len(p) == 0:
        print(X)
        return

    i = 0
    while True:
        if X - i not in p:
            print(X - i)
            return
        elif X + i not in p:
            print(X + i)
            return
        else:
            i += 1

if __name__ == "__main__":
    main()
