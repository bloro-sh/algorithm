def solution(array):
    array.sort() #오름차순 정렬 전체 배열에서 //2
    answer = len(array)
    result = answer//2 #1 -> 이제 값을 꺼내야함
    return array[result]

i = [1,2,7,10,11]
b = [9,-1,0]
add = solution(b)
print(add)