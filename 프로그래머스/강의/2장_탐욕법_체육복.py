def solution(n, lost, reserve):
    u = [1] * (n+2)
    for i in reserve:
        u[i] += 1
    for i in lost:
        u[i] -= 1
    for i in range(1,n+1):
        if u[i - 1] == 0 and u[i] == 2:
            u[i - 1:i + 1] = [1,1]
        elif u[i] == 2 and u[i+1] == 0:     # boundary check를 하지 않기 위해
            u[i:i+2] = [1,1]
    return len([x for x in u[1:-1] if x >0])

# 방법 2
# set은 value는 없고 자료가 속해있는지 없는지만 확인해
def solution(n, lost, reserve):
    s = set(lost) & set(reserve)
    l = set(lost) - s # l에는 체육복을 도난당해서 체육복을 빌려야하는 사람만 들어있습니다.
    r = set(reserve) -  s # 빌려줄 수 있는 학생들
    for x in sorted(r):
        if x - 1 in l:
            l.remove(x - 1)
        elif x + 1 in l:
            l.remove(x + 1)
    return n - len(l) # l에는 빌려야하는데 빌리지 못한 학생들이 남게 됩니다.

