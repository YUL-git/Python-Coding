1. 특정 조건, 왼쪽과 오른쪽의 합이 동일하면 발동
2. 중간 지점을 찾는 일 길이의 중간(기준)을 정해야해
n = input()
left = n[:len(n)//2]
right = n[len(n)//2:]
left_count = 0
right_count = 0
for i in left:
    left_count += int(i)
for i in right:
    right_count += int(i)
if str(left_count) == str(right_count):
    print('LUCKY')
else:
    print('READY')