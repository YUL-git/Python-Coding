'''
토마토가 모두 익을 때까지 최소 날짜를 출력해야합니다.
이때 사용하면 좋은 알고리즘은 bfs입니다. 상하좌우로 동시에 익은 토마토가
전염시키기 때문입니다. 그런데 -1이라는 토마토가 들어있지 않은 칸이 있는데 이때
bfs를 전부 통과시키고 나서 0이 있다면 -1로 막혀 있는 것임으로 -1을 반환해줍니다.
1의 위치를 파악하는게 최우선 과제네
'''
from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i,j))

while q:
    y, x = q.popleft()
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if nx < 0 or ny < 0 or nx >= m or ny >= n:
            continue
        if graph[ny][nx] == -1:
            continue
        if graph[ny][nx] == 0:
            graph[ny][nx] = graph[y][x] + 1
            q.append((ny, nx))

least = 0
breaker = False
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            least = -1
            breaker = True
            break
        else:
            least = max(graph[i][j], least)
    if breaker == True:
        print(-1)
        break
else:
    print(least - 1)