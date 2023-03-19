'''
bfs를 구현 최소한의 경로의 길이를 어떻게 구할 것인가?
인접 노드들을 전부 다 방문하고 나서 count를 해주면 되겠다.
'''
from collections import deque

n,m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

def bfs(x,y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    print(graph)
    return graph[n-1][m-1]
print(bfs(0,0))