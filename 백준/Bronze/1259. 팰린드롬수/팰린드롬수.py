num_list = []
count = 0
while 1 :
    num = input()
    if num == '0' :
        break
    num_list.append(num)
    # print(num_list)
for i in range(len(num_list)) :
    for j in range(len(num_list[i])//2) :
        if num_list[i][j] == num_list[i][-j-1] :
            count += 1
        # print(count)
    if count == len(num_list[i])//2 :
        print('yes')
    else :
        print('no')
    count = 0