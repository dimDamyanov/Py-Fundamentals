def valid(username):
    if 3 <= len(username) <= 16:
        for c in username:
            if not (c.isalnum() or c in '-_'):
                return False
    else:
        return False
    return True


data = input().split(', ')
[print(u) for u in data if valid(u)]