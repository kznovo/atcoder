# TODO

K = int(input())
S = input()

insert = len(S) + 1
print((insert ** insert * (26**insert)) % (10 ** 9 + 7))
