from math import sqrt


class Vector:
    def __init__(self, coords_list: list):
        self.coords_list = coords_list

    def __str__(self):
        return f"{str(tuple(self.coords_list)).replace(' ','')}"

    def equals(self, other):
        return self.coords_list == other.coords_list

    def is_comparable(self, other):
        if len(self.coords_list) == len(other.coords_list):
            return True
        raise ValueError

    def add(self, other):
        if self.is_comparable(other):
            return Vector([self.coords_list[i] + other.coords_list[i] for i in range(len(self.coords_list))])

    def subtract(self, other):
        if self.is_comparable(other):
            return Vector([self.coords_list[i] - other.coords_list[i] for i in range(len(self.coords_list))])

    def dot(self, other):
        if self.is_comparable(other):
            return sum([self.coords_list[i] * other.coords_list[i] for i in range(len(self.coords_list))])

    def norm(self):
        return sqrt(sum(map(lambda x: x ** 2, self.coords_list)))