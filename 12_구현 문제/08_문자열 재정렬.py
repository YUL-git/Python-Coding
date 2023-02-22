1. 문자열과 알파벳 구별하기
2. 문자열 정렬하기
3. 구분 기준

number = ['0','1','2','3','4','5','6','7','8','9']
n = input()
v = []
e = []
for i in n:
    if i in number:
        v.append(int(i))
    else:
        e.append(i)
s = sum(v)
e.sort()
e.append(s)
for i in e:
    print(i,end='')
