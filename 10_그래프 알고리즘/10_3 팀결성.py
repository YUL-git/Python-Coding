# 나의 풀이
1. 팀 합치기 연산 함수
2. 같은 팀 여부 확인 연산 --> NO/YES

n,m = map(int, input().split())
parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_team(a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def same_team(a,b):
    if find_parent(parent, a) != find_parent(parent,b):
        print('NO')
    else:
        print('YES')

for _ in range(m):
    num,a,b = map(int, input().split())
    if num == 0:
        union_team(a,b)
    elif num == 1:
        same_team(a,b)
    else:
        print('Unable input')