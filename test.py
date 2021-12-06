a=1
b=1
while True:
    a = int(input('a: '))
    b = int(input('b: '))

    if b>100:
        print(b,'is too big!')
        break

    
    if a%b ==0:
        print(f'{a} is divided by {b}')
    elif a%b!=0:
        print(f'{a} is not divided by {b}')

    
