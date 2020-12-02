input_type = input()
value = input()


def type_print(type_, val):
    if type_ == 'int':
        print(int(val) * 2)
    elif type_ == 'real':
        print('%.2f' % (float(val) * 1.5))
    elif type_ == 'string':
        print(f'${val}$')


type_print(input_type, value)
