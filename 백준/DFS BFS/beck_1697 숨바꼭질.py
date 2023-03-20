'''
수빈이의 위치에서 동생에게 갈 수 있는 모든 방법을 다 활용해보고난 후
가장 작은 값을 꺼내서 출력한다.
bfs를 사용하여 각 위치에서 할 수 있는 3가지 방법을 모두 que에 삽입
선형 배열이 필요해 동생으로가는 선형 배열과 이동하는 방법에 따른 계산 방법 3가지를 구현해줘야해
기존에 있던 숫자와 도달했을 때 걸린 시간과 더 작은 값을 저장
'''

from collections import deque
def bfs(n,m):
    visit = [int(float(1e5))] * int(float(1e5))
    visit[n] = 0
    q = deque()
    q.append((n, n + 1))
    q.append((n, n - 1))
    q.append((n, n * 2))
    while q:
        past, now = q.popleft()
        if now == m:
            visit[now] = min(visit[now], visit[past] + 1)
            return visit[now]
        elif now >= 0 and now <= int(float(1e5)):
            visit[now] = min(visit[now], visit[past] + 1)
            q.append((now, now + 1))
            q.append((now, now - 1))
            q.append((now, now * 2))

n, m = input().split()
n = int(float(n))
m = int(float(m))
print(bfs(n, m))

from collections import deque

def bfs(n, m):
    visit = [int(1e9)] * 100001
    visit[n] = 0
    q = deque()
    q.append(n)
    while q:
        now = q.popleft()
        if now == m:
            return visit[now]
        for next_pos in [now-1, now+1, now*2]:
            if 0 <= next_pos <= 100000 and visit[next_pos] > visit[now] + 1:
                visit[next_pos] = visit[now] + 1
                q.append(next_pos)

n, m = map(int, input().split())
print(bfs(n, m))


