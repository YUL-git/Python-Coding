'''
1. calculate 함수를 정의하자. 이 함수는 순차적으로 연산자의 우선 순위를 무시하고 계산을 하는 함수이다
2. 자료구조로써 큐를 선택하자. 먼저 나온 것이 먼저 반환됨으로 que를 사용하자.
3. 해당 배열에 담긴 숫자가 모두 사용될 때까지 반복하자.
4. 연산자의 조합은 어떻게 생성할 것인가? -> 순열을 사용하자.
 4-1. 순열을 사용할 때는 해시로 key값에 개수 value를 특성으로 받고 key값의 순열을 활용하자
5. 각 각의 연산자의 조합에 따른 값들을 answer 리스트에 추가하고 가장 큰 결과와 작은 결과를 출력해주자.
'''
from collections import deque
# calculate 함수
def calculate(number_list, cal_list):
    n = deque()
    c = deque()
    for i in cal_list:
        c.append(i)
    for i in number_list:
        n.append(i)
        if len(n) == 2:
            n1 = n.popleft()
            n2 = n.popleft()
            cal = c.popleft()
            if cal == '+':
                answer = n1 + n2
                n.append(answer)
            elif cal == '-':
                answer = n1 - n2
                n.append(answer)
            elif cal == '*':
                answer = n1 * n2
                n.append(answer)
            else:
                if n1 < 0:
                    answer = -(abs(n1) // n2)
                    n.append(answer)
                else:
                    answer = n1 // n2
                    n.append(answer)
    return n.pop()

# 연산자 조합
'''
4. 연산자의 조합은 어떻게 생성할 것인가? -> 순열을 사용하자.
 4-1. 순열을 사용할 때는 해시로 key값에 개수 value를 특성으로 받고 key값의 순열을 활용하자
 '''
from itertools import permutations
n = int(input())
number_list = list(map(int, input().split()))
cal_list = list(map(int,input().split()))
cal = ['+','-','*','//']
a = []
result = []
for x,y in zip(cal,cal_list):
    for _ in range(y):
        if y > 0:
            a.append(x)
z = set(permutations(a))
'''
5. 각 각의 연산자의 조합에 따른 값들을 answer 리스트에 추가하고 가장 큰 결과와 작은 결과를 출력해주자.
'''
for i in z:
    c = calculate(number_list,i)
    result.append(c)
print(max(result))
print(min(result))

# --------------
def dfs(num, p, m, t, d, idx):
    if idx == n - 1:
        global max_res, min_res
        if num > max_res:
            max_res = num
        if num < min_res:
            min_res = num
        return

    if p:
        dfs(num + num_list[idx + 1], p - 1, m, t, d, idx + 1)
    if m:
        dfs(num - num_list[idx + 1], p, m - 1, t, d, idx + 1)
    if t:
        dfs(num * num_list[idx + 1], p, m, t - 1, d, idx + 1)
    if d:
        dfs(int(num/num_list[idx + 1]), p, m, t, d - 1, idx + 1)
