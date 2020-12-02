num = float(input())
if num == 0:
    print('zero')
elif -1 < num < 0:
    print('small negative')
elif num < -1_000_000:
    print('large negative')
elif num < 0:
    print('negative')
elif 0 < num < 1:
    print('small positive')
elif num > 1_000_000:
    print('large positive')
elif num > 0:
    print('positive')
