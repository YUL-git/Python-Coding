# 나의 풀이
from itertools import combinations
n,m = map(int, input().split())
weight = list(map(int,input().split()))
a = list(combinations(weight,2))
count = 0
for i in a:
    if i[0] != i[1]:
        count += 1
print(count)

## 해답
# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m+1):
    n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += array[i] *n # B가 선택하는 경우의 수와 곱하기
print(result)