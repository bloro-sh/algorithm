def solution(numbers):# 배열에 있는것을 하나씩 꺼내고 2배로 곱한다음 다시 리스트에 저장

    answer = [] #리스트 저장용
    b = 0
    for i in numbers: #배열에 있는것 하나씩 값 꺼내기
        b = i*2 #4를 리스트에 넣음
        answer.append(b)
    return answer

b =[1, 2, 3, 4, 5] #10만 나오는이유는 추가를 안해서 최종 10만 나오는거임
a = solution(b)
print(a)