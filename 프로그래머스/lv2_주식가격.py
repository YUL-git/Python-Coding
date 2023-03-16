# 나의 풀이
'''
deque는 slice를 지원하지 않는다.
이 부분에서 시간을 많이 빼앗김
'''
'''
효율성 문제로 탈락
'''
# 나의 풀이
from collections import deque
def solution(prices):
    prices = deque(prices)
    num = len(prices)
    time = []
    while prices:
        val = prices.popleft()
        num -= 1                            # 이렇게 지정하면 시간이 더 빨라질거라 생각
        if num > 0:                         # --> 여기서 쓸데없이 for문에 공백 리스트가 걸릴까봐 걱정해서
            for i in range(num):            # 새로운 변수 sec을 추가해주면 덱의 값끼리 비교할 수 있었지,
                if val > prices[i]:         # 덱 값의 인덱스를 알기위해 prices.index(i)를 사용할 생각을 했어
                    time.append(i+1)
                    break
            else:
                time.append(num)
        else:
            time.append(0)
            break
    return time
## 정정 풀이 1
from collections import deque
def solution(prices):
    prices = deque(prices)
    time = []
    while prices:
        val = prices.popleft()  #O(1)
        sec = 0                 # prices의 인덱스 값으로 활용할 sec 변수를 만듬
        for i in prices:        # for문으로 받을 때 prices가 공백이라면 그냥 아무값도 나오지 않아
            sec += 1
            if val > i:
                break
        time.append(sec)        # 해당 sec값을 time에 저장
    return time

## 정정풀이 2
def solution(prices):
    length = len(prices)
    answer = [i for i in range(length - 1, -1, -1)]

    stack = [0]
    for i in range(1, length, 1):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer
