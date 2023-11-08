def left_right_sum_eq(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i + 1:]):
            return i
    return -1


print(left_right_sum_eq([1, 2, 3, 4, 3, 2, 1]))
print(left_right_sum_eq([1, 100, 50, -51, 1, 1]))
print(left_right_sum_eq([20, 10, -80, 10, 10, 15, 35]))