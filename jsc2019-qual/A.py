def takahashi_cal(m: int, d: int) -> int:
    res = 0
    for mm in range(1, m + 1):
        for dd in range(1, d + 1):
            d1 = dd % 10
            d10 = dd // 10
            if any([d1 < 2, d10 < 2]):
                continue
            if d1 * d10 == mm:
                res += 1
    return res
    
m, d = input().split(" ")
print(takahashi_cal(int(m), int(d)))