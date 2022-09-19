finding_target = 2
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# 처음 숫자와 마지막 숫자의 합에서 //2 몫이 타겟보다 큰지 작은지에 따라 기준 숫자 변경


def is_existing_target_number_binary(target, array):
    # 구현해보세요!
    max_number = array[-1]
    min_number = array[0]
    

    while min_number <= max_number:
        center_number = (max_number + min_number) //2
        if center_number < target:
            min_number = center_number + 1
        elif center_number > target:
            max_number = center_number - 1
        elif center_number == target:
            return True

    

    return False



result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)