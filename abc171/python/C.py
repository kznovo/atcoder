import string

N = int(input()) - 1
smap = dict(enumerate(string.ascii_lowercase))

res = []
while True:
    d, m = divmod(N, 26)
    res.append(m)
    if d-1 > 25:
        N = d-1
    else:
        if d == 0:
            break
        else:
            res.append(d-1)
            break

print("".join(smap[i] for i in reversed(res)))

