money = 1000 - int(input())
type = [500,100,50,10,5,1]
count = 0

for i in range(len(type)) : #500
    count += money // type[i]
    money = money % type[i] 
print(count)