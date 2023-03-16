def solution(L, x):
    if x in L:
        return [i for i, v in enumerate(L) if v == x]
    else:
        return [-1]