N = int(input())
div, mod = divmod(N, 1000)
if mod > 0:
    print(1000 - mod)
else:
    print(0)
