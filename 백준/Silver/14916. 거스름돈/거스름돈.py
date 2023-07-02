n = int(input())
count = 0
if n == 1 or n == 3 :
    print(-1)
elif (n % 5) % 2 == 0 : #5로 나눈 나머지가 짝수일 때
    count += n // 5
    n = n % 5
    count += n // 2
    print(count)
else : #13 % 5 = 3 -> 3 + 5 = 8 -> 4
    count = n // 5
    n = (n % 5) + 5
    count += n // 2

    print(count-1)