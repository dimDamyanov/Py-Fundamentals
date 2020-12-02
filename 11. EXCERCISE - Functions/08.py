n = int(input())


def loading_bar(percent):
    a = percent // 10
    return f'{percent}% [{"%" * a}{"." * (10 - a )}]\nStill loading...' if percent != 100 else '100% Complete!\n[%%%%%%%%%%]'


print(loading_bar(n))