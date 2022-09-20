array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    num1 = 0
    num2 = 0
    total_array = []
    while num1 < len(array1) and num2 < len(array2):
        if array1[num1] < array2[num2]:
            total_array.append(array1[num1])
            num1+=1
            
        else:
            total_array.append(array2[num2])
            num2+=1
            
    if num1 == len(array1):
        while num2 <len(array2):
            total_array.append(array2[num2])
            num2+=1
    if num2 == len(array2):
        while num1 <len(array1):
            total_array.append(array1[num1])
            num1+=1
    return total_array
   


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge([-7, -1, 9, 40], [5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge([-1,2,3,5,40], [10,78,100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge([-1,-1,0], [1, 6, 9, 10]))