import sys

def Fn(depth, idx) :
    if depth == 6 :
        for i in result_list :
            print(i, end=' ')
        print('')
        return
    for jdx in range(idx, k) :
        result_list[depth] = lotto_list[jdx]
        Fn(depth+1, jdx+1)

while True :
    case_list = list(map(int, sys.stdin.readline().split()))
    k = case_list[0]
    lotto_list = case_list[1:]
    if k == 0:
        break
    result_list = [0 for _ in range(6)]
    # print(lotto_list)
    Fn(0,0)
    print()