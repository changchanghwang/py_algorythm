input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    exists = number in array
    return exists


result = is_number_exist(3, input)
print(result)