print("소인수분해 함수 추가")

def prime_fact(a=1):

    b=a
    i=2
    plist = list()

    while b!=1:

        while b%i == 0:
            b = b/i
            plist.append(i)
        i+=1
    if plist==[]:
        plist=[a]

    return(plist)
