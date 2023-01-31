import time
n = int(input())
array = [int(input()) for _ in range(n)]
start_time = time.time()
for i in range(n):
    max_index = i
    for j in range(i+1,n):
        if array[max_index] < array[j]:
            max_index = j
    array[max_index], array[i] = array[i], array[max_index]
print(array)
end_time = time.time()
print(end_time-start_time)
# 풀이
n = int(input())

array = [int(input()) for _ in range(n)]
array = sorted(array, reverse=True)         # 그냥 sorted로 정렬해버림
for i in array:
    print(i, end=' ')