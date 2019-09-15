import heapq

n, m = map(int, input().split(" "))

a = [- int(i) for i in input().split(" ")]
heapq.heapify(a)

for _ in range(m):
    largest = heapq.heappop(a)
    heapq.heappush(a, int(largest / 2))

print(- sum(a))

