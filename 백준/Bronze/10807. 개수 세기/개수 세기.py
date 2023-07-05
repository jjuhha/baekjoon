
n = int(input())
n_list = list(map(int, input().split()))
target = int(input())

count = n_list.count(target)

print(count)