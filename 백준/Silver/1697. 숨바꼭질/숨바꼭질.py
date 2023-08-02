from collections import deque
import sys
N, K = map(int, sys.stdin.readline().split())
location_check = [0 for _ in range(100001)]
location_check[N] = 1
que = deque()
que.append((N,0))

# print(que)
count = 0

while len(que) != 0 : #동시다발적으로 뻗어가야하는데 하나씩 팝하는게 문제
    subin, count = que.popleft()
    if subin == K :
        # count += 1
        break
    if subin+1 <= 100000 :
        if location_check[subin+1] != 1 :
            que.append((subin+1,count+1))
            location_check[subin + 1] = 1
    if subin-1 >= 0:
        if location_check[subin - 1] != 1 :
            que.append((subin-1,count+1))
            location_check[subin - 1] = 1
    if 2*subin <= 100000:
        if location_check[2*subin] != 1 :
            que.append((2*subin,count+1))
            location_check[2*subin] = 1
    # print(que)
# count += 1
print(count)