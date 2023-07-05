N, X = map(int,input().split())
n_list = list(map(int, input().split()))
result = []

for i in range(N) :
    if n_list[i] < X :
        result.append(n_list[i])
for j in range(len(result)) :
    print(result[j], end=' ')