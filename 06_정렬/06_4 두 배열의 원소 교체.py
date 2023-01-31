# 1. 배열 A는 오름차순 정렬
# 2. 배열 B는 내림차순 정렬
# 3. 값 스와이프
# 4. K번만큼 수행
n, k = map(int, input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort(reverse=True)
for i in range(k):
    min_a = a[i]                # 이부분은 정말 말도 안되는 코드 운이 좋았다.
    a[i] = b[i]                 # 정렬한 b의 값이 a 값보다 작을 수도 있는데 고려하지 않았어
    b[i] = min_a
print(sum(a))

# 풀이
for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break                   # break해야 이제 더이상 b에 a보다 큰 값이 없음으로 sum(a)를 하는 것이 최댓값임