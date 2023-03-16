n = int(input())
m = list(map(int, input().split()))
'''
소수의 조건
1. 자기자신과 1을 제외한 나머지 수는 나눌 수 없다
'''
cnt = 0
for x in m:
    result = []
    for y in range(2,1001):
        if x%y == 0:
            result.append(y)
    else:
        if len(result) == 1:
            cnt += 1
print(cnt)