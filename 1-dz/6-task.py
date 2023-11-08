def max_int(num: int):
    digits = [int(i) for i in str(num)]

    def quick_sort_reversed(arr):
        if not arr:
            return []
        lower_then = []
        higher_then = []
        middle_num = len(arr) // 2
        for i in arr[:middle_num] + arr[middle_num + 1:]:
            if i > arr[middle_num]:
                lower_then.append(i)
            else:
                higher_then.append(i)
        lower_sorted = quick_sort_reversed(lower_then)
        higher_sorted = quick_sort_reversed(higher_then)
        return lower_sorted + [arr[middle_num]] + higher_sorted

    return int("".join(map(str, quick_sort_reversed(digits))))


print(max_int(128951234567890345678907890138492948720987656))
