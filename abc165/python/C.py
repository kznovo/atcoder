from itertools import combinations_with_replacement

N, M, Q = [int(i) for i in input().split()]

q_list = []
for _ in range(Q):
    a, b, c, d = input().split()
    q_list.append([int(a), int(b), int(c), int(d)])

max_pts = 0
for A in combinations_with_replacement(range(1, M + 1), N):
    pts = 0
    for (a, b, c, d) in q_list:
        if A[b - 1] - A[a - 1] == c:
            pts += d
    max_pts = max(max_pts, pts)

print(max_pts)
