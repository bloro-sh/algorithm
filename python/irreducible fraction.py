def solution(numer1, denom1, numer2, denom2):

    numer1 = numer1 * denom2 #분자 4
    numer2 = numer2 * denom1 #분자 6

    denom1 = denom1*denom2 #분모 8
    num = numer1+numer2 #분자 10 = 10/8

    b=0
    for i in range(1,min(denom1,num)+1):#최대공약수 선정하기 = 8
        if num % i == 0 and denom1 % i ==0: # 공약수 가 나와야됨(1,2,5,10)1,2,3 공통 공약수 2
            b = i #b에 2를 넣음
    denom1 = denom1 // b
    num = num //b



    return num,denom1

n,denom = solution(1,2,3,4)
print(n,denom)