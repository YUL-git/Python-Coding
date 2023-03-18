'''
1. 괄호검사!
2. 단 괄호검사시 중간에 숫자가 있다면 저장
3. 괄호 검사 탈락시 바로 0 출력
4. 괄호 검사 통과시 괄호검사 점수와 숫자의 곱을 다시 저장
5. 이하 반복
6. array의 괄호를 모두 다쓰면 stack에 있는 것을 검사 이때 숫자는 모두 더하고
괄호가 나올 시에 0을 출력
'''

from collections import deque
from sys import stdin
def check(array):
    stack = deque()
    if not array:
        return 0
    array = deque(array)
    while array:
        if array[0] in ['(','[']:
            stack.append(array.popleft())
        elif array[0] in [')',']'] and stack:
            if stack[-1] == '(' and array[0] == ')':
                stack.pop()
                array.popleft()
            elif stack[-1] == '[' and array[0] == ']':
                stack.pop()
                array.popleft()
            else:
                return 0
        else:
            return 0
    if len(stack):
        return 0
    return True

array = [i for i in stdin.readline().rstrip()]

def solution(array):
    if check(array):
        stack = deque()
        array = deque(array)
        while array:
            if array[0] in ['(','[']:
                stack.append(array.popleft())
            else:
                i = 0
                while stack:
                    if stack[-1] == '(' and array[0] == ')':
                        stack.pop()
                        array.popleft()
                        if i != 0:
                            stack.append(2*i)
                            break
                        else:
                            stack.append(2)
                            break
                    elif stack[-1] == '[' and array[0] == ']':
                        stack.pop()
                        array.popleft()
                        if i != 0:
                            stack.append(3*i)
                            break
                        else:
                            stack.append(3)
                            break
                    else:
                        i += stack.pop()
        return sum(stack)
    else:
        return 0
print(solution(array))