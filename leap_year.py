print('leap_year')

while True:
    year = int(input('연도를 입력하세요: '))

    if year==0:
        print('프로그램을 종료합니다.')
        break

    if year % 4 != 0:
        leap='평'
    elif year % 100 !=0:
        leap='윤'
    elif year % 400 !=0:
        leap = '평'
    else:
        leap = '윤'

    print(f'{year}년은 {leap}년입니다.')
