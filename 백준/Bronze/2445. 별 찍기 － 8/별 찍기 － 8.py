a = int(input())
for i in range(a) :
    print("*"*(i+1)+" "*(2*(a-1-i))+"*"*(i+1))
for j in range(a-1) :
    print("*"*(a-1-j)+" "*(2*j+2)+"*"*(a-1-j))