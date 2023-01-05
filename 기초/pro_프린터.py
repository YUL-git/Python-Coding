# 나의 풀이(왜 안되는거지?)
'''
내 코드의 오류
가장 큰 값의 위치가 결정 되는 순간에
출력 순서가 결정 되는 것으로 판단
하지만, 지속적으로 내가 원하는 순서에 있는 숫자의
몇 번째에 출력 되는 지가 궁금한 것임
'''

# def findMaxIndex(priorities):
#     if not len(priorities):
#         return None
#     else:
#         highest = 0
#         for i in range(1,len(priorities)):
#             if priorities[i] > priorities[highest]:
#                 highest = i
#         return highest
#
# def solution(priorities, location):
#     highest = findMaxIndex(priorities)
#     if location > highest:
#         a = len(priorities[highest:location])+1
#     elif location == highest:
#         a = 1
#     else:
#         a = len(priorities[highest:])+location+1
#     return a
#
# priorities = [1,1,4,1,1,1,1,1,3,2]
# location = 5
# a = solution(priorities,location)
# print(a)
# b = findMaxIndex(priorities)
# print(b)

## 정정한 풀이 1
# location에 있는 숫자가 몇 번째에 출력될 것인가
# pop은 언제 되는가? -> 최댓값이 대기 리스트에 존재 할 때
def solution(priorities, location):
    temp = deque([(i,v) for v,i in enumerate(priorities)]) # i는 우선순위 값,v는 인덱스 값
    ans = 0
    while temp:
        val = temp.popleft()
        if temp and val[0] < max(temp)[0]:
            temp.append(val)
        else:
            ans += 1
            if val[1] == location:
                break
    return ans
## 정정한 풀이2 (any 사용)
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

## 교과서 같은 우선순위 탐색 방법
def solution(priorities, location):
    jobs = len(priorities)
    answer = 0
    cursor = 0
    while True:
        if max(priorities) == priorities[cursor%jobs]:
            priorities[cursor%jobs] = 0
            answer += 1
            if cursor%jobs == location:
                break
        cursor += 1
    return answer
