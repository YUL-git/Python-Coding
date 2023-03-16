# try - except문을 활용해서 특정 key값에 대한 index값을 비교할 수 있도록 코드를 구현
def solution(keymap, targets):
    answer = []
    keymap_redesign = {}
    for k in keymap:
        k = list(k)
        for i in range(len(k)):
            try:
                if keymap_redesign[k[i]] > i + 1:
                    keymap_redesign[k[i]] = i + 1
            except:
                keymap_redesign[k[i]] = i + 1
    for x in targets:
        n = 0
        for each in x:
            if each in keymap_redesign:
                n += keymap_redesign[each]
            else:
                answer.append(-1)
                break
        else:
            answer.append(n)
    return answer