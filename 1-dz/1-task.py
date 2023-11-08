import time
import math

def time_dec(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        worktime = time.time() - start
        print(f"{worktime} seconds passed")
        return result

    return wrapper


@time_dec
def sum_of_all_multiples_1(max_num):
    result = 0
    for num in range(3, max_num):
        if num % 3 == 0 or num % 5 == 0:
            result += num
    return result


@time_dec
def sum_of_all_multiples_2(max_num):
    def sum_of_mult(num, count):
        sum_all_count = (count * (count + 1)) // 2  #сума арифметичної прогресії
        return sum_all_count * num

    max_num -= 1
    count_3 = max_num // 3
    count_5 = max_num // 5
    count_15 = max_num // 15
    return sum_of_mult(3, count_3) + sum_of_mult(5, count_5) - sum_of_mult(15, count_15)


print(sum_of_all_multiples_2(math.factorial(859)))
