def largest_honor(arr, d):
    list_of_sums = []
    for i in range(len(arr) // d):
        list_of_sums.append(sum(arr[i::len(arr) // d]))
    return max(list_of_sums)


print(largest_honor([1, 2, 3, 4], 2))
print(largest_honor([1, 5, 6, 3, 4, 2, 8, 9], 2))
print(largest_honor([2, 6, -7, 8], 1))