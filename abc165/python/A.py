K = int(input())
A, B = [int(i) for i in input().split()]

if any(i % K == 0 for i in range(A, B + 1)):
    print("OK")
else:
    print("NG")
