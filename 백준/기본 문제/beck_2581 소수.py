'''
1. 예를 들어 새로운 리스트로 1이상 10이하의 자연수가 나오면
2. 1,2,3,4,5,6,7,8,9,10 에서 2,3,5,7를 뽑아서 더해준다.
3. 첫째줄에는 총 합을 출력하고
4. 둘째줄에는 최솟값을 출력한다
소수를 뽑는 기준을 정해야한다.
소수는 1 또는 나 자신을 제외한 숫자로 나누어지지 않는 수이다.
'''
n = int(input())
m = int(input())
result = []
final = []
for i in range(n,m+1):
    result.append(i)

for i in result:
    cnt = 0
    for j in range(2, i+1):
        if i % j == 0:
            cnt += 1
    else:
        if cnt == 1:
            final.append(i)
if len(final) == 0:
    print(-1)
else:
    print(sum(final))
    print(min(final))

