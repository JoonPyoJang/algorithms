
input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    
    count = 0
    while count <= len(array)-2:
        for i in range(1,len(array)-count):
            if array[i-1] > array[i]:
                array[i-1],array[i] = array[i], array[i-1]
        count += 1 
    
    return array

bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",bubble_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",bubble_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",bubble_sort([100,56,-3,32,44]))
