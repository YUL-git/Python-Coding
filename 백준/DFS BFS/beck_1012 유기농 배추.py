import sys
sys.setrecursionlimit(10000)
# 상하좌우 움직임 저장
dx = [1,-1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(y, x):
    visited[y][x] = True
    for i in range(4):
        rx = dx[i] + x
        ry = dy[i] + y
        if rx < 0 or rx >= m or ry < 0 or ry >= n:
            continue
        if world[ry][rx] == 1 and not visited[ry][rx]:
            dfs(ry, rx)

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    # 유기농 배추의 world를 생성
    world = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    cnt = 0

    # 유기농 배추가 있는 곳에 1을 표시
    for i in range(k):
        x, y = map(int, input().split())
        world[y][x] = 1

    # dfs()를 통해서 유기농 배추를 지렁이로 관리할 수 있는 구역 개수 구하기
    for i in range(n):
        for j in range(m):
            if world[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                cnt += 1
    print(cnt)