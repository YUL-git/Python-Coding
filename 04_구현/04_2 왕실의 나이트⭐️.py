# 1. a,b,c,d 를 어떻게 하지?
#
n = input()
n = [i for i in n]
dx = int(n[1])
dy = n[0]
a = ['a','b','c','d','e','f','g','h']
for i in range(len(a)):
    if dy == a[i]:
        n = i+1
move_types = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
x, y = (n, dx)
count = 0
for i in range(len(move_types)):
    nx, ny = x + move_types[i][0], y + move_types[i][1]
    if nx < 1 or ny < 1 or nx > 8 or ny >8 :
        continue
    count +=1
print(count)

# 풀이
## 현재 위치 입력 받기
input_data = input()
row = int(input_data[1])                                # 일반 string에서도 index를 사용할 수 있어
column = int(ord(input_data[0])) - int(ord('a')) + 1    # 아스키 코드로 변경하는 방법 (외우자)
steps = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1
print(result)