# 예제 4-1
n = int(input())
x, y =1,1
plans = input().split()

dx = [0,0,-1,1]
dy = [1,-1,0,0]
move_types = ['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
print(x,y)

# 예제 4-2
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count +=1
print(count)

# 왕실의 나이트
result = 0
for step in steps