password_input = input()


def is_valid(password: str):
    valid = True
    if not 6 <= len(password) <= 10:
        print('Password must be between 6 and 10 characters')
        valid = False
    if not password.isalnum():
        print('Password must consist only of letters and digits')
        valid = False
    if sum(c.isnumeric() for c in password) < 2:
        print('Password must have at least 2 digits')
        valid = False
    return valid


if is_valid(password_input):
    print('Password is valid')