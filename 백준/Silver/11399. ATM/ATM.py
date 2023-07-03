num = int(input())
m_list = list(map(int,input().split()))
result = 0

m_list.sort()

for i in range(num) : #0 #1 #2 #3 #4 #5
    for j in range(i+1) : #0 #0,1 #0,1,2 #0,1,2,3 #0,1,2,3,4
        result += m_list[j]
print(result)