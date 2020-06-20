S = input()
N = len(S)

def isPalindrome(s):
    return s == s[::-1]

left = S[:N//2]
right = S[(N+2)//2:]
if isPalindrome(S) and (left == right):
    print("Yes")
else:
    print("No")

