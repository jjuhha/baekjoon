import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T) :
    count = 0
    n = int(input())
    que = deque()
    que.append((n,count))
    count += 1
    counts = 0
    while len(que) != 0 :
        n, count = que.popleft()
        if n == 0 :
            counts += 1
        if n >= 1 :
            que.append((n-1, count+1))
        if n >= 2 :
            que.append((n-2, count+1))
        if n >= 3 :
            que.append((n-3, count+1))
    print(counts)