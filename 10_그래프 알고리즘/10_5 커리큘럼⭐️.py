import copy

1. 위상 정렬
진입 차수 개념이 중요함
1. 진입차수가 0인 노드를 큐에 넣는다
2. 큐가 빌 대까지 다음의 과정을
if 반복한다:
    1. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다
    2. 새롭게 진입차수가 0이 된 노드를 큐에
    if 넣는다:

from collections import deque

v = int(input())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(v+1)]
# 각 강의 시간을 0으로 초기화
time = [0] *(v+1)

# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(1,v+1):
    data = list(map(int, input().split()))
    time[i] = data[0] # 첫 번째 수는 시간 정보를 담고 있음
    for x in data[1:-1]:
        indegree[i] += 1
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = copy.deepcopy(time) # 알고리즘 수행 결과를 담을 리스트
    q = deque()

    for i in range(1,v+1):
        if indegree[i] == 0
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i],result[now]+time[i])
            indegree[i] -= 1
            if indegree == 0:
                q.append(i)
    for i in range(1, v+1):
        print(result[i])
topology_sort()