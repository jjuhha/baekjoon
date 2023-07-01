a, b = map(int, input().split()) 

week_list = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
day_list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
result = 0

for i in range(a) :
    result += day_list[i]
    
result += b

print(week_list[result%7])