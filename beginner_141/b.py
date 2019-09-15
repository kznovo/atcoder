s = input()
out = "No" if any(ss not in "RUD" for ss in s[::2]) or any(ss not in "LUD" for ss in s[1::2]) else "Yes"
print(out)

