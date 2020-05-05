from collections import deque

def main():
    K = int(input())
    if K <= 9:
        print(K)
        return

    que = deque(range(1,10))
    # print(que)
    cnt = 9
    while True:
        x = que.popleft()
        mod = x % 10

        if mod != 0:
            que.append(10 * x + mod - 1)
            # print(que)
            cnt += 1
            if cnt == K:
                print(que[-1])
                return

        que.append(10 * x + mod)
        # print(que)
        cnt += 1
        if cnt == K:
            print(que[-1])
            return

        if mod != 9:
            que.append(10 * x + mod + 1)
            # print(que)
            cnt += 1
            if cnt == K:
                print(que[-1])
                return

main()
