c_start = input()
c_end = input()


def ascii_in_between(start, end):
    return ' '.join(chr(i) for i in range(ord(start) + 1, ord(end)))


print(ascii_in_between(c_start, c_end))