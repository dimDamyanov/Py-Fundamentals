operator = input()
n1 = int(input())
n2 = int(input())


def calculate(operation, a, b):
    if operation == 'multiply':
        return a * b
    elif operation == 'divide':
        res = str(a / b)
        return res.rstrip('.0') if '.' in res else res
    elif operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b


print(calculate(operator, n1, n2))