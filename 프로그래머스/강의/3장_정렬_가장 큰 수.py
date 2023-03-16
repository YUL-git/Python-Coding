# 숫자의 크기를 어떻게 비교하지? 정수의 비교가 아니라 문자열로 나열했을 때의 크기를 비교해야해
# 3 30 34
def solution(numbers):
    s = []
    numbers.sort(key=lambda x: str(x)[0], reverse=True)
    for i in numbers:
        i = str(i)
        s.append(int((i * 4)[0:4]))
    s.sort(reverse=True)
    return print(s, end='')

def solution(numbers):
    numbers = [str(x) for x in numbers]
    numbers.sort(key=lambda x : (x * 4)[:4], reverse=True)
    if numbers[0] == '0':
        answer = '0'
    else:
        answer = ''.join(numbers)
    return answer

2610
6210
62
26