# 나의 풀이
N = int(input())
'''
파이썬은 if문에서 
empty list는 False를
empty가 아닌 list는 True를 리턴
'''
for _ in range(N):
    a = input()
    stack = []
    for i in a:
        if i != ')':
            stack.append(i)
        elif i == ')':
            if stack:           # stack이 공백이라면 실행이 안돼
                stack.pop()
            else:
                print('NO')
                break
    # break문으로 끊기지 않고 수행됬을 경우 수행한다.
    else:
        if not stack: # break문으로 안끊기고 스택이 비어있다면 괄호가 다 맞는거임
            print('YES')
        else:
            print('NO')
    # for-else
    '''
    for와 함께 쓰는 else는, for문이 중간에 break 등으로 끊기지 않고,
    끝까지 수행 되었을 때 수행하는 코드를 담고 있습니다.
    '''