def number_of_cubs(m):
    volume = 0
    n = 1
    while volume <= m:
        if volume == m:
            return n - 1
        volume += n ** 3
        n += 1
    return -1


print(number_of_cubs(1071225))
print(number_of_cubs(91716553919377))
