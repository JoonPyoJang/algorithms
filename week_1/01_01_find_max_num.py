input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    array.sort()

    return array[-1]

result = find_max_num(input)
print(result)