# 두수를 제거한다 -> 두 수를 뺀 나머지를 선택한다 -> 조합
# 무식한 방법!!
from itertools import combinations
def solution(number,k):
    n = list(combinations(number, len(number)-k))
    answer = []
    for x in n:
        answer.append(''.join(x))
    answer.sort(reverse=True)
    return answer[0]
### 시간초과가 걸려 + 숫자의 순서 관계가 깨지면 안되는 것을 고려하지 않았어
'''
1231234
가장 큰 수가 들어있는 인덱스를 뽑고 해당 인덱스들을 다시 재배열해서 가장 큰 수를 만든다? enumerate 사용
'''
# 각 자리 수에서 가장 큰 수만 고를 수 있다면?
# 어떻게 앞에서부터 더 작은 숫자가 나오는 것을 빼 줄 수 있을까?
# 앞 자리에 큰 수가 오는 것이 전체를 크게 만든다. -> 큰 것을 골라서 가고 싶다
# 1924, k = 2
# 1231234 k = 3 작은 것을 빼되 앞에서 작은 것을 빼야하지 뒤에서 작은 것은 빼지 않아
def solution(number, k):
    answer = []
    for i,v in enumerate(number):
        answer.append([v,i])
    answer.sort(reverse=True)
    answer = answer[:len(answer)-k]
    answer.sort(key=lambda x : x[1])
    n = ''
    for x in range(len(answer)):
        n += answer[x][0]
    return n


def solution(number, k):
    collected = []
    for i, num in enumerate(number):
        while len(collected) > 0 and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1
        if k == 0:
            collected += list(number[i:])
            break
        collected.append(num)
    collected  = collected[:-k] if k > 0 else collected
    answer = ''.join(collected)
    return answer