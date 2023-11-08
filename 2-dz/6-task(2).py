from typing import List


def island_per(island: List[str]):
    result = 0
    next_coords = []
    for x in range(len(island)):
        for y in range(len(island[0])):
            if island[x][y] == "X":
                if y:
                    if island[x][y - 1] == "X": result -= 2
                if (x, y) in next_coords: result -= 2
                result += 4
                next_coords.append((x + 1, y))
    return result


island = ['XOOXO',
          'XOOXO',
          'OOOXO',
          'XXOXO',
          'OXOOO']

island_2 = ['XOOO',
            'XOXO',
            'XOXO',
            'OOXX',
            'OOOO']

print(island_per(island))
print(island_per(island_2))