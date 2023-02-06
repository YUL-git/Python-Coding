# 내림차순으로 구현하기
# 파이썬에서는 오름차순으로 제공
import heapq
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h,-value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1,4,3,2,4,6,8,4,9])
print(result)