1.  2개의 최소 신장 트리 만들기
2. 크루스칼 알고리을 사용해서 그래프를 만들고
3. 그중에서 가장 비용이 큰 길을 삭제

1. 크루스칼 알고리즘 함수
2. 비용삭제
3. trivial solution

1. 크루스칼 알고리즘
1. 간선 데이터를 비용에 따라 오름차순으로 정렬
2. 사이클이 발생시키는지 확인
3. 모든 간선에 대해서 반복

def find_parent(parent, x):
    if parent[x] !=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a< b:
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int, input().split())
parent = [0] *(v+1)

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

for i in range(1,n+1):
    parent[i] = i

for _ in range(m):
    a,b,c = map(int,input().split())
    edges[a].append((c,a,b))

# 간선을 비용순으로 정렬
edges.sort()
last = 0 # 최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선

for edge in edges:
    c,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent, a,b)
        result += c
        last = c

print(result - last)