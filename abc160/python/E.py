# TODO

X, Y, A, B, C = [int(i) for i in input().split()]
P = sorted(int(i) for i in input().split())
Q = sorted(int(i) for i in input().split())
R = sorted(int(i) for i in input().split())

res = 0

while True:
    if X > 0 and len(P) > 0:
        p_max = max(P)
        if len(R) > 0 and p_max > max(R):
            res += p_max
            X -= 1
            P.pop()
            continue
    
    if Y > 0 and len(Q) > 0:
        q_max = max(Q)
        if len(R) > 0 and q_max > max(R):
            res += q_max
            Y -= 1
            Q.pop()
            continue
    
    


    