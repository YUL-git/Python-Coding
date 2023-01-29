# 나는 서로 다른 인덱스의 반복을 같은 인덱스의 곱으로 하려함
# counter의 숫자를 이용해서 풀려고 함
# 그리고 k만큼 반복하는 것을 어떻게 해야할 지 몰랐음

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1
print(result)

## 수열의 관점
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
first = data[n-1]
second = data[n-2]

count = int(m/(k+1))*k
count += m%(k+1)

result = 0
result += (count)*first
result += (m-count)*second

print(result)