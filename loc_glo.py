x=50
def func():
    #global x # 전역변수
    print( 'x is',x)
    x=2
    print('Changed global x to',x)

func()
