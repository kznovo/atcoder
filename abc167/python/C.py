from itertools import combinations

def main():
    N, M, X = [int(i) for i in input().split()]
    C, A = [], []
    for _ in range(N):
        ca = [int(i) for i in input().split()]
        C.append(ca[0])
        A.append(ca[1:])

    for m in range(M):
        if sum(a[m] for a in A) < X:
            print(-1)
            return

    sets = []
    comb_ix = [comb for i in range(1, len(A) + 1) for comb in combinations(range(len(A)), i)]
    for m in range(M):
        tmp_lst = []

        for comb in comb_ix:
            a = [a[m] for i, a in enumerate(A) if i in comb]
            if sum(a) >= X:
                tmp_lst.append(comb)
        
        sets.append(frozenset(tmp_lst))

    intersection = set.intersection(*map(set, sets))
    res = sum(C)
    for comb in intersection:
        sum_c = sum(c for i, c in enumerate(C) if i in comb)
        if sum_c < res:
            res = sum_c

    print(res)

main()
