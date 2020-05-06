X = int(input())

div500, mod500 = divmod(X, 500)
div5 = mod500 // 5

print(div500 * 1000 + div5 * 5)
