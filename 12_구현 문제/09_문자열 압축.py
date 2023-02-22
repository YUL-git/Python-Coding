# 해설
'''
1. 문자열 길이/2개의 단위로 잘라 압축하는 경우를 시도
2. 그 중에서 가장 짧은 길이의 문자열의 길이 출력
3. 반복되는 문자열을 어떻게 찾을 것인가, scan을 단위만큼 slicing해서 다음에도 반복이 되는지 확인하기
'''
def solution(s):
    answer = len(s)
    # 각 단위별로 슬라이싱해서 찾아보기 i단위의 슬라이스
    for step in range(1,len(s)//2 + 1):
        compressed = ""
        prev = s[0:step] # 앞에서부터 step만큼의 문자열 추출
        count = 1
        for j in range(step,len(s),step):
            # 이전 상태와 동일하다면 압축 횟수 증가
            if prev == s[j:j+step]:
                count += 1
            # 다른 문자열이 나왔다면
            else:
                compressed += str(count) + prev if count>=2 else prev
                prev = s[j:j+step]
                count = 1
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    return answer



# 다른 풀이
def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):   # 공백을 준 이유는 비교 대상이 없으면 에러가 나기 때문에
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

a = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",

    'aaaaaa',
]

for x in a:
    print(solution(x))


