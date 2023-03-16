n,m = map(int,input().split())
'''
1이면 1번 반복
2면 2번 반복
3이면 3번 반복...
각각의 인덱스를 개수로 하여 곱셈연산을 진행
숫자가 10일 경우 1010101010을 어떻게 처리?
'''
result = [0]
cnt = 0
for i in range(1, m+1):
    for _ in range(i):
        result.append(i)
for i in range(n,m+1):
    cnt += result[i]
print(cnt)