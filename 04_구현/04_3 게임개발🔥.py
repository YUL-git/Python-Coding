# 나의 풀이
n, m = map(int, input().split())
a, b, d = map(int, input().split())

game_map = []
for i in range(n):
    row = list(map(int,input().split()))
    game_map.append(row)

x , y = a, b
way = [0,1,2,3]
steps = [(-1,0),(0,1),(1,0),(0,-1)]

count = 1
while True:
    game_map[x][y] = 1
    for i in range(len(way)):
        if d == way[i]:
            dx = x + steps[i][0]
            dy = y + steps[i][1]
        if game_map[dx][dy] == 1:
            d = (d+1) % 4
            continue
        x , y = dx, dy
        count += 1

# 풀이
n, m = map(int, input().split())
# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]             # 컴프리핸션으로 지도를 만듬
# 현재 캐릭터의 x 좌표, y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1,0,1,0]                 # 방향을 정의하는 방법을 x,y 인덱스로 표현
dy = [0,1,0,-1]                 # 방향을 이동하는 방법이 정해져 있다면 tuple형태로 받고 아니면 dx,dy형식으로 지정

# 왼쪽으로 회전
def turn_left():                # 회전하는 함수를 생성한 것
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
# 시뮬레이션 시작
count = 1
turn_time = 0                   # turn_time을 주어서 더이상 갈 곳이 없다는 것을 구현해냄
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny]==0 and array[nx][ny] == 0:     # array와 d를 따로 지정해서 맵에 변형을 주지 않는 방법
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:              # 더 이상 갈 곳이 없다는 것을 turn_time으로 구현함
        nx = x-dx[direction]
        ny = y-dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤로 바다로 막혀있는 경우
        else:
            break
        turn_time = 0
print(count)