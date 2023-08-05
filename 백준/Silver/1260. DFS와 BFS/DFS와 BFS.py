import sys
from collections import deque
n, m, v = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
for i in range(m) :
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(1, n+1) :
    graph[i].sort()
# print(graph)

def dfs(start) :
    stack = [] #방문할 노드를 넣어줄 빈 리스트
    visit = [0 for _ in range(n+1)] #방문여부 표시할 리스트
    # [0,0,0,0,0]
    stack.append(start)

    while len(stack) > 0 :
        curr = stack[-1]
        if visit[curr] == 0 :
            print(curr, end=' ')
            visit[curr] = 1
        flag = False
        for nxt in graph[curr] :
            if visit[nxt] == 0 :
                stack.append(nxt)
                # print(stack)
                flag = True
                break
        if flag == False :
            stack.pop()

dfs(v)

def bfs(start) :
    queue = deque()
    visited = [0 for _ in range(n+1)]
    queue.append(start)
    visited[start] = 1

    while len(queue) > 0 :
        curr = queue[0]
        print(curr, end=' ')
        for nxt in graph[curr] :
            if visited[nxt] == 0 :
                visited[nxt] = 1
                queue.append(nxt)
        queue.popleft()
print()
bfs(v)