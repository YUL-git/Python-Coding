'''
목표) 만들 수 없는 최소의 금액
알고리즘) 주어진 동전중에서 가장 큰 동전 n이라고 했을 때 n이하의 숫자중에 동전의 조합을 제외한 후 최솟값을 뽑으면 돼
'''
n = int(input())
coin_types = list(map(int,input().split()))
target = 1
for i in coin_types:
    if target < coin_types:
        break
    target += i
return target
