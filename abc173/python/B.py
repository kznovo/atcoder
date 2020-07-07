N = int(input())
S = {"AC": 0, "WA": 0, "TLE": 0, "RE": 0}
for _ in range(N):
    c = input()
    if c in S:
        S[c] += 1

for k, v in S.items():
    print(f"{k} x {v}")
