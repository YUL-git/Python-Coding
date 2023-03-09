# 해시를 어떻게 이용하느냐?
def solution(participant, completion):
    d = {}
    for x in participant:
        d[x] = d.get(x, 0) + 1 # .get(key,값)
    for x in completion:
        d[x] -= 1           # 해당하는 이름의 값을 빼줘
    dnf = [k for k, v in d.items() if v > 0] # list comprehension
    answer = dnf[0]
    return answer

# 정렬을 이용한다면?
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant)-1]