'''
dfs를 활용해야한다.
dfs를 통해서 각 칸을 이동하는 횟수를 구하고 이 횟수중 가장 작은 횟수를 출력한다.
여기서 문제가 dfs가 실행된 횟수중 가장 작은 횟수를 어떻게 구할지가 문제
'''
from collections import deque
move_list = [(-2, 1),(-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

def min_moves(l, start, end):
    queue = deque([(start,0)])
    visited = set(start)
    while queue:
        current, moves = queue.popleft()
        if current == end:
            return moves
        for move in move_list:
            next_pos = (current[0] + move[0], current[1] + move[1])
            if next_pos[0] < 0 or next_pos[0] >= l or next_pos[1] < 0 or next_pos[1] >= l:
                continue
            if next_pos in visited:
                continue
            visited.add(next_pos)
            queue.append((next_pos, moves + 1))
    return -1

t = int(input())
for _ in range(t):
    l = int(input())
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    print(min_moves(l,start,end))