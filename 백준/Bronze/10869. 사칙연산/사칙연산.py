#첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.

A, B = input().split()
a = int(A)
b = int(B)

print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
print(a%b)