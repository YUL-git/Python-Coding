# deque의 rotate를 사용
from collections import deque
import sys
n = [i for i in range(1,int(sys.stdin.readline().rstrip())+1)]
n = deque(n)
while len(n)>1 :
    n.popleft()
    n.rotate(-1)
print(n[0])