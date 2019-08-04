#!/usr/bin/env python3


def f(txy):
    pt, px, py = txy[0]
    
    if pt < (px + py) or sum([pt % 2, px % 2, py % 2]) % 2:
        print("No")
        return
    
    else:
        for t, x, y in txy[1:]:
            mvt, mvx, mvy = t - pt, x - px, y - py
            if mvt < (mvx + mvy) or sum([mvt % 2, mvx % 2, mvy % 2]) % 2:
                print("No")
                return
            pt, px, py = t, x, y
        
        print("Yes")


N = int(input())
txy = [tuple(int(i) for i in input().split(" ")) for _ in range(N)]
f(txy)
