n = int(input())
for _ in range(n):
    m = list(map(int, input().split()))
    m.sort(reverse=True)
    print(m[2])