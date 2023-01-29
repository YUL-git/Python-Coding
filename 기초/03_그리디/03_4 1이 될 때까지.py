n, k = map(int, input().split())
count = 0
while n > 1:
    if n % k != 0:
        n -= 1
        count +=1
    else:
        n /= k
        count +=1
print(count)

# 풀이 1
n, k = map(int, input().split())
result = 0

while n >= k:
    while n%k !=0:
        n-=1
        result +=1
    n //= k
    result +=1
while n >1:
    n -=1
    rsult += 1
print(result)

# 풀이 2
n, k = map(int, input().split())
result = 0

while True:
    target = (n//k)*k
    result += (n-target)
    n = target

    if n<k:
        break
    result +=1
    n //= k
result += (n-1)
print(result)
