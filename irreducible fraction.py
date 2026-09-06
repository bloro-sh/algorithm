def solution(numer1, denom1, numer2, denom2):

    numer1 = numer1 * denom2 #분자 4
    numer2 = numer2 * denom1 #분자 6

    denom1= denom1 * denom2 #분모 8
    a = numer1+numer2 #분자 10 
    #10/8을 기약분수로 하려면? 답은 5/4
    b=0
    for i in range(1,min(denom1,a)+1):#8구하기
        if a % i==0 and denom1 % i ==0:#분자 분모 나머지가0인게 같은것 공약수 2 반환
            b = i #2를 b에 넣음
    denom1 = denom1//b #분모
    a = a//b #분자
    
    
    return denom1,a

denom,num = solution(1,2,3,4)
print(num,denom)