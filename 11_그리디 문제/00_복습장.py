# 1. 모험가 길드
'''
공포도 보다 그룹에 있는 인원수가 같거나 많다면 그룹 달성 만약 그렇지 않다면 그룹 계속해서 팀원을 모아줘
공포도와 그룹의 인원수를 셀 수 있는 수단 이 필요해
몇 번 동안 진행 할거야? 총 인원수 만큼 진행을 해보고 안되면 그냥 스킵되니까 상관없지
'''
n = int(input())
array = list(map(int,input().split()))
array.sort()
count = 0
group = 0
for i in array:
    count += 1
    # 공포도와 그룹의 인원 수를 비교
    if i <= count:
        group += 1
        count = 0
print(group)

# 2. 곱하기 혹은 더하기
'''
0과 1일 때는 곱하기를 하지 않고 더하기 연산을 진행, 나머지는 곱하기
그러면 해당 숫자가 1보다 큰지 작은지를 판단해야해
현재의 숫자와 for 루프문으로 들어온 숫자 중에 1보다 작거나 같은 값이 하나라도 있다면
더하기 연산을 진행
'''

n = list(map(int,input()))
result = 0
now = n[0]
for i in range(1,len(n)):
    if now <= 1 or n[i] <=1:
        now += n[i]
    else:
        now *= n[i]
print(now)

# 3. 문자열 뒤집기
'''
최소한으로 뒤집는 숫자를 비교해서 둘 중 더 작은 수를 선택
숫자가 바뀔 때마다 뒤집는 횟수를 추가해줘
'''
n = input()
count0 = 0
count1 = 0
if n[0] != '0':
    count0 += 1
else:
    count1 += 1
for i in range(1,len(n)):
    # 0으로 뒤집는 경우
    if n[i] != '0' and n[i-1] =='0':
        count0 += 1
    if n[i] != '1' and n[i-1] == '1':
        count1 += 1
print(min(count0,count1))

##
for i in range(len(n)-1):
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            count0 += 1
        else:
            count1 += 1

# 4. 만들 수 없는 금액
'''
정렬을 하고 target을 정하자 1~ target-1까지는 만들 수 있는 금액이라고 가정하자
만약에 다음에 들어오는 동전이 target보다 크다면 해당 target은 만들 수 없는 금액이다
'''
n = int(input())
coin = list(map(int, input().split()))
coin.sort()
target = 1
for i in coin:
    if target >= i:
        target += i
    else:
        break
print(target)
## 조금 더 가시적으로 코딩
for x in coin:
    if target < x:
        break
    target += x

# 5. 볼링공 고르기
array = [0] * 11
for x in data:
    array[x] += 1
result = 0
for i in range(1, m+1):
    n -= array[i]
    result += array[i] * n
print(result)

# 6. 무지 먹방
'''
음식을 먹는 소요 시간을 정렬해
만약에 소요시간  x 음식의 종류 < k 다면 
가장 적은 소요 시간을 음식을 먹는데 걸리는 시간과 음식의 종류만큼 k에서 빼줘
만약에 소요시간 x 음식의 종류 > k 라면
이제 빼지 않고 음식의 종류대로 다시 정렬해준 다음에 해당 남은 나머지 만큼의 인덱스를 반환해줘
'''
# 무지의 먹방 라이브
import heapq


def solution(food_times, k):
    answer = -1
    h = []
    for i in range(len(food_times)):
        heapq.heappush(h, (food_times[i], i + 1))

    food_num = len(food_times)  # 남은 음식 개수
    previous = 0  # 이전에 제거한 음식의 food_time

    while h:
        # 먹는데 걸리는 시간: (남은 양) * (남은 음식 개수)
        t = (h[0][0] - previous) * food_num
        # 시간이 남을 경우 현재 음식 빼기
        if k >= t:
            k -= t
            previous, _ = heapq.heappop(h)
            food_num -= 1
        # 시간이 부족할 경우(음식을 다 못먹을 경우) 남은 음식 중에 먹어야 할 음식 찾기
        else:
            idx = k % food_num
            h.sort(key=lambda x: x[1])
            answer = h[idx][1]
            break

    return answer