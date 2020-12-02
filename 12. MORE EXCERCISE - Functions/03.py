from math import sqrt, pow

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())


def sort_points(x_1, y_1, x_2, y_2):
    distance_a = sqrt(pow(x_1, 2) + pow(y_1, 2))
    distance_b = sqrt(pow(x_2, 2) + pow(y_2, 2))
    return ((int(x_1), int(y_1)), (int(x_2), int(y_2))) if distance_a <= distance_b \
        else ((int(x_2), int(y_2)), (int(x_1), int(y_1)))


def longer_line(x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4):
    length_a = sqrt(pow((x_1 - x_2), 2) + pow((y_1 - y_2), 2))
    length_b = sqrt(pow((x_3 - x_4), 2) + pow((y_3 - y_4), 2))
    return sort_points(x_1, y_1, x_2, y_2) if length_a >= length_b else sort_points(x_3, y_3, x_4, y_4)


print(*longer_line(x1, y1, x2, y2, x3, y3, x4, y4), sep='')