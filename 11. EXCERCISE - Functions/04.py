num = int(input())


def digit_sum(n):
    odd_sum = 0
    even_sum = 0
    digits = list(map(int, str(n)))
    for digit in digits:
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
    return odd_sum, even_sum


res = digit_sum(num)
print(f'Odd sum = {res[0]}, Even sum = {res[1]}')