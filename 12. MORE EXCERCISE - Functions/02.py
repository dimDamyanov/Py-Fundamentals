from math import sqrt, pow
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())


def closest_point(a: tuple, b: tuple):
    distance_a = sqrt(pow(a[0], 2) + pow(a[1], 2))
    distance_b = sqrt(pow(b[0], 2) + pow(b[1], 2))
    return tuple(map(int, a)) if distance_a < distance_b else tuple(map(int, b))


print(closest_point((x1, y1), (x2, y2)))
