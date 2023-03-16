# 정렬을 할때 대소문자가 구분되어 있어서 제대로 counter의 역할을 하지 못함
# sys.stdin.readline()만 쓰면 우측 공백이 생겨서 \n이 같이 적힘 rstrip()을 무조건 해줘야해
from collections import Counter
import sys
string = sys.stdin.readline().rstrip().lower()
max = Counter(string).most_common(2)
if len(string)==1:
    print(string.upper())
else:
    if max[0][1] == max[1][1]:
        print('?')
    else:
        print(max[0][0].upper())