# 1. 이진 탐색
n = int(input())
array = list(map(int, input().split()))
array.sort() # 이진 탐색을 수행하기 위해 사전에 정렬 수행
m = int(input())
want = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    result = binary_search(array,i,o,n-1)
    if result != None:
        print('yes',end=' ')
    else:
        print('no',end=' ')

# 2. 계수 정렬
n = int(input())
array = [0] *1000001
for i in input().split():           # 이런 방식으로 input()을 받을 수 있구나
    array[int(i)] = 1
m = int(input())
want = list(map(int, input().split()))

#손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    if array[i] == 1:
        print('yes',end=' ')
    else:
        print('no',end=' ')

# 3. 집합 자료형 이용
n = int(input())
array = list(map(int, input().split()))
m = int(input())
want = list(map(int, input().split()))

for i in range(m):
    if want[i]  in array:
        print('yes',end=' ')
    else:
        print('no',end=' ')