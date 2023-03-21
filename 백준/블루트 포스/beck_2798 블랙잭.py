from itertools import combinations
n, m = map(int, input().split())
num = list(map(int, input().split()))

k = list(combinations(num, 3))
a = []
b = []
for i in k:
    s = sum(i)
    if s <= m:
        a.append(abs(s-m))
        b.append(s)
idx = a.index(min(a))
print(b[idx])
