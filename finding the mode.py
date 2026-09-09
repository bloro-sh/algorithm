def solution(array):
    result = {}
    for number in array: #array에 있는 값을 number로 넣기
        if number in result:
            result[number] +=1
        else:
            result[number] = 1

        add = 0 #가장 많이 가지고 있는 수

        for key,value in result.items():
            if value > add:#값이 add보다 큰 경우
                add = value#add에 넣어라
        count = 0
        mode = 0
        for key, value in result.items():#중복값 검사
            if add == value:#add의 값이랑 값이 같을때
                count+=1
                mode = key

        if count>=2:
            return -1
        return mode

a = [1, 2, 3, 3, 3, 4]
result = solution(a)
print(result)