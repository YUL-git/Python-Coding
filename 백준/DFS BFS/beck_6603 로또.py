'''
집합 S가 주어지면 6개를 뽑으면 된다. 여기서 6개의 조합을 출력해야한다.
출력은 사전순으로 출력해야한다.
각 테스트 케이스 사이에는 빈 줄을 출력해야하고
마지막의 입력으로는 0을 받는다.

규칙성:

'''
from itertools import combinations
while True:
    test_case = list(map(int, input().split()))
    if test_case[0] == 0:
        break
    test = list(combinations(test_case[1:], 6))
    for i in test:
        for j in i:
            print(j, end = ' ')
        print()
    print()

# DFS/ BFS
def dfs(comb, start, s):
    if len(comb) == 6:
        print(*comb)
        return
    for i in range(start,len(s)):
        comb.append(s[i])
        dfs(comb, i + 1, s)
        comb.pop()
while True:
    lst = list(map(int, input().split()))
    if lst[0] == 0:
        break
    k = lst[0]
    s = lst[1:]
    dfs([],0,s)
    print()