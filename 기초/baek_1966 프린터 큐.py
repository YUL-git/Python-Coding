from collections import deque
n = int(input()) # n번의 test를 할거야
for _ in range(n):
    N,M = map(int, input().split())
    priorites = list(map(int,input().split()))
    temp = deque([(v,i) for i,v in enumerate(priorites)])
    ans = 0
    while temp:
        val = temp.popleft()
        if temp and val[0] < max(temp)[0]:
            temp.append(val)
        else:
            ans += 1
            if val[1] == M:
                print(ans)
                break


