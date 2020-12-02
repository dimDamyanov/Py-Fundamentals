line = input()
coffee = 0
while not line == 'END':
    if line.casefold() == 'coding' or line.casefold() == 'dog' \
            or line.casefold() == 'cat' or line.casefold() == 'movie':
        if line.isupper():
            coffee += 2
        else:
            coffee += 1
    line = input()
if coffee > 5:
    print('You need extra sleep')
else:
    print(coffee)
