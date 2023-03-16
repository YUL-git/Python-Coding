# que 를 이용(선입 선출)
# 경과시간 -> 트럭 대수(다리의 무게 이하일 경우) + 다리의 길이
# sum(bridge)로 다리위의 트럭 무게를 더하게 되면 시간 초과가 됨
from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge_weight = 0                                   # 다리 위의 트럭 무게
    waiting = deque(truck_weights)                      # 대기 트럭 큐
    bridge = deque([0 for _ in range(bridge_length)])   # 다리의 길이 큐
    while len(waiting) or bridge_weight > 0:            # 다리에 트럭이 올라갈 수 있다면
        removed_truck = bridge.popleft()                # bridge에 공간 하나를 제거하고
        bridge_weight -= removed_truck                  # bridge_weight는 removed_truck만큼 가벼워짐

        if len(waiting) and bridge_weight + waiting[0] <= weight:   # 올라갈 트럭이 있고 올라갈 수 있다면
            new_truck = waiting.popleft()                           # 새로운 트럭이 대기 트럭에서 뽑힘
            bridge_weight += new_truck                              # 다리 무게는 추가

            bridge.append(new_truck)                                # bridge에 new_truck을 추가
        else:                                                       # 트럭이 올라갈 수 없다면
            bridge.append(0)                            # 다시 0을 추가(bridge_length의 길이 맞춰주기)

        time += 1                                       # 시간은 계속 흘러감
    return time


