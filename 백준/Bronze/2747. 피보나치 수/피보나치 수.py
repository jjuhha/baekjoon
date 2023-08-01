n = int(input())
n_list = [0,1,]

for i in range(2,n+1) :
    n_list.append(n_list[i-1] + n_list[i-2])

print(n_list[-1])