import heapq

특정 노드에서 특정 노드로 가는 최단 경로 -> 다익스트라 알고리즘
1. heapq을 이용하자
2. distance, graph(인접 노드)를 생성
3. 특정 노드에서 다른 노드를 거쳐서 가는 경로가 가까운 경우 최적화

INF = int(1e9)
n,m = map(int,input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]
for a in range(1, n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b] = 0
for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x,k = map(int,input().split())

for k in range(1,n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
distance = graph[1][k] + graph[k][x]
if distance >= INF:
    print('-1')
else:
    print(distance)