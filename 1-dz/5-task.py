import math


def highAndLow(strng: str):
    min_num = math.inf
    max_num = -min_num
    num_list = tuple(map(int, strng.split()))
    for num in num_list:
        max_num = num if num > max_num else max_num
        min_num = num if num < min_num else min_num
    return f"{max_num} {min_num}"


print(highAndLow("1 2 3 4 5"))
print(highAndLow("1 9 3 4 -5"))
