from copy import deepcopy
from itertools import combinations, product

H, W, K = map(int, input().split())
board = []
for _ in range(H):
    row = input()
    row = [r == "#" for r in row]
    board.append(row)

all_h_comb = [()]
for r in range(1, H):
    comb_obj = combinations(range(H), r)
    all_h_comb += list(comb_obj)
all_w_comb = [()]
for c in range(1, W):
    comb_obj = combinations(range(W), c)
    all_w_comb += list(comb_obj)
all_comb = list(product(all_h_comb, all_w_comb))

res = 0
for comb in all_comb:
    r, c = comb
    tmp_board = deepcopy(board)
    for _r in r:
        tmp_board[_r] = [False] * W
    for _c in c:
        for b in tmp_board:
            b[_c] = False
    s = sum(sum(l) for l in tmp_board)
    if s == K:
        res += 1
print(res)

