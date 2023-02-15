목표) 그룹 수의 최댓값
알고리즘) 현재 포함된 그룹의 인원수가 해당 공포도 보다 크거나 같다면 그룹 구성
# 자꾸 counter를 사용해서 해당 값과 개수를 비교하여 같으면 1을 추가해주려고 하다 보니 구현이 안됌
n = int(input())
array = list(map(int,input().split()))
array.sort()
# 현재 포함된 그룹의 인원수
count = 0
# 그룹의 수
result = 0
for i in array:
    count += 1
    if count >= i:      #  알고리즘
        result += 1     # 그룹 결성
        count = 0       # 현재 그룹에 포함된 인원수 초기화
print(result)