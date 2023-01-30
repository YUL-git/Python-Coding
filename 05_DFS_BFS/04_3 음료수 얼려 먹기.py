n, m = map(int, input().split())
# 지도
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
# 좌표
graph = []
for i in range(n):
    for j in range(m):
        graph.append([i,j])
# 방문 여부
visited=[]
for _ in range(n):
    visited.append([False] * m)

dx = [-1,1,0,0]
dy = [0,0,1,-1]


# 어? v가 내가 원하는 정수 v가 아니라 좌표로 표현해야하는 것인가? 그래프로 어떻게 만들지?
def dfs(array, graph, v , visited):
    visited[v[0]][v[1]] = True
    for i in range(4)
        nx = v[0] + dx[i]
        ny = v[1] + dy[i]
        if array[nx][ny] != 1 and visited[nx][ny] == False and nx>0 and ny>0 and nx<n and ny <m:
            v = [nx,ny]
            dfs(array,graph,v,visited)
# 피드백
'''
1. dfs의 입력값으로 무조건 graph를 줄 생각만 했어
2. 상하좌우의 움직임을 따로 만들어 놓은 dx, dy를 통해서 수동으로 옮겨주고 dfs 함수에 넣을려고 했어
3. 좌표를 단순히 x,y로 놓지 않고 복잡하게 리스트로 만들었어
4. dfs를 재귀적으로 부르는데 아이스크림의 완성을 어떻게 표현해야 할 지 
 True/False를 반환하여 True일 경우에 result+=1을 생각하지 못했어 
5. 조건을 줄 때 모두 True일 때 실행 보다 어느 하나라도 포함될 때 False를 주는게 더 좋은거 같아
'''
# 풀이
'''
1. 특정한 지점의 주변 상, 하, 좌, 우를 살펴본 뒤에 주변 지점 중에서 값이 '0'이면서 
아직 방문하지 않은 지점이 있다면 해당 지점을 방문한다.
2. 방문한 지점에서 다시 상, 하, 좌, 우를 살펴 보면서 방문을 다시 진행하면, 연결된 모든 지점을 방문할 수 있다.
3. 1~2번의 과정을 모든 노드에 반복 하며 방문하지 않은 지점의 수를 센다.
'''

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

def dfs(x,y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x>= n or y<= -1 or y >=m:
        return False
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        #현재 위치에서 DFS수행
        if dfs(i,j) == True:
            result +=1
print(result)