n, m = map(int, input().split())
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    if min(data) > result:                      #이 부분은 max(result, min_value)로 바꿔주기
        result = min(data)
print(result)

# 풀이 1
n, m = map(int, input().split())
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result,min_value)
print(result)

# 풀이 2
n, m = map(int, input().split())
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:                  #현재 줄에서 '가장 작은 수' 찾기
        min_value = min(min_value,a)
    result = max(result,min_value)
print(result)