def counter_moves_1(n, start, finish):
    counter = 0

    def Hanoi_moves(n, start, finish):
        nonlocal counter
        if n <= 0:
            return
        counter += 1
        temp = 6 - start - finish
        Hanoi_moves(n - 1, start, temp)
        print(f"{n}-size figure from {start} to {finish}")
        Hanoi_moves(n - 1, temp, finish)

    Hanoi_moves(n, start, finish)
    return counter


def counter_moves_2(n):
    return 2 ** n - 1


print(counter_moves_1(4, 1, 3))
print(counter_moves_2(4))