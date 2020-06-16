def main():
	N = int(input())
	A = [int(i) for i in input().split()]
	
	if 0 in A:
		print(0)
		return
	
	res = 1
	top = 10 ** 18
	for a in A:
		res *= a
		if res > top:
			print(-1)
			return
	print(res)

if __name__ == "__main__":
	main()

