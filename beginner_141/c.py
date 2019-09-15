n, k, q = map(int, input().split(" "))
 
init = k - q
ns = [init] * n
 
for _ in range(q):
    ns[int(input()) - 1] += 1
 
for i_n in ns:
    if i_n > 0:
        print("Yes")
    else:
        print("No")
