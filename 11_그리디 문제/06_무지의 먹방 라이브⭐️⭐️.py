'''
가장 작은 것을 통으로 빼야겠다고 생각 했으나 정렬하지 않고 그냥 리스트에 해당 min값을 계속 해서
몫만큼 뺄려고 하는 순간 리스트에 빼기 때문에 음수가 만들어졌고 효율성 테스트에서 가장 작은 index를 찾는 과정
이 있음으로 통과하지 못함
'''
import heapq
def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1

    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i+1))

    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식시간
    length = len(food_times) # 남은 음식의 개수

    # sum_value + (현재의 음식 시간 - 이전 음식시간) * 현재 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous)*length <= k):
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now
    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key=lambda x: x[1])
    return result[(k-sum_value)%length][1]
