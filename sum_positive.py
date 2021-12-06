print('sum_positive')
n=0

while True:
    n1 = int(input('양수만 입력(음수 입력시 오류): '))

    if n1>0:
        n+=n1
    elif n1==0:
        break

    print('중간 합계 = ',n)

print('최종 합계 = ',n)
