'''
dfs를 통해 한 번의 dfs가 끝나면 cnt를 + 1 해준다.
이때 visited 라는 리스트가 필요하고 인접행렬 리스트도 필요하다.
dfs를 실행할 때 visited가 False이고 인접행렬의 값이 있을 때만 실행한다는 조건을 걸어준다
'''
import sys
sys.setrecursionlimit(10000)
def dfs(node, visited, graph):
    if visited[node] == False:
        visited[node] = True
        for i in range(len(graph[node])):
            if visited[graph[node][i]] == False:
                dfs(graph[node][i], visited, graph)

n, m = map(int, input().split())
adj = [list(map(int, input().split())) for _ in range(m)]
visited = [False] * (n + 1)
graph = {i: [] for i in range(1, n+1)} # 요소가 1일때 에러가 났었어
for x, y in adj:
    graph[x].append(y)
    graph[y].append(x)


cnt = 0
for x in range(1, n + 1):
    if visited[x] == False:
        dfs(x, visited, graph)
        cnt += 1
print(cnt)