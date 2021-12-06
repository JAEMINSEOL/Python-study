print('Korean_1_to_3')

num = 1
while True:
    num=int(input('1-3사이의 숫자를 입력: '))
    if num==1:
        kor='일'
    elif num==2:
        kor='이'
    elif num==3:
        kor='삼'
    else:
        print('범위 벗어남!')
        break
    print(f'{num}은 한국어로 {kor}(이)라고 부릅니다')
    
