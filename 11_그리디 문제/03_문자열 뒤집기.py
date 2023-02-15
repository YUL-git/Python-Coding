'''
목표) 행동의 최소 횟수
알고리즘)
1. 분할이 가장 덜 된 0 or 1을 뒤집음
2. 연속된 숫자가 끊기면 하나의 분할이 생긴 것

연속된 숫자임을 어떻게 알지?
--> 같지 않을 경우에만 특정 조건을 준다면 조건이 실행되지 않을 때는 연속됐다고 볼 수 있어
'''
n = input()
count0 = 0
count1 = 0
# 첫 번째 원소 처리
if n[0] == '1':
    count0 += 1
else:
    count1 += 1
for i in range(len(n)-1):
    if n[i] != n[i+1]:
        # 1로 바꾸는 경우
        if n[i] == '0':
            count1 += 1
        # 0으로 바꾸는 경우
        else:
            count0 += 1
print(min(count0,count1))


