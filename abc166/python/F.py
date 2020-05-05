def main():
    N, A, B, C = [int(i) for i in input().split()]

    if A == B == C == 0:
        print("No")
        return

    S = [input() for _ in range(N)]
    d = {"A": A, "B": B, "C": C}
    order = []

    for i, s in enumerate(S):
        s1, s2 = s

        if d[s1] == d[s2] == 0:
            print("No")
            return
        elif d[s1] == 0:
            d[s1] += 1
            d[s2] -= 1
            order.append(s1)
        elif d[s2] == 0:
            d[s2] += 1
            d[s1] -= 1
            order.append(s2)
        elif d[s1] == d[s2] == 1:
            try:
                if s1 in S[i + 1]:
                    d[s1] += 1
                    d[s2] -= 1
                    order.append(s1)
                else:
                    d[s2] += 1
                    d[s1] -= 1
                    order.append(s2)
            except:
                order.append(s1)
        else:
            if d[s1] > d[s2]:
                d[s1] -= 1
                d[s2] += 1
                order.append(s2)
            else:
                d[s2] -= 1
                d[s1] += 1
                order.append(s1)
    
    print("Yes")
    for o in order:
        print(o)


main()
