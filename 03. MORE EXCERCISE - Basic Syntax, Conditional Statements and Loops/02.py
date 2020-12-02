s = input()


def get_indices(string):
    return [i for i, c in enumerate(string) if c.isupper()]


capitals = get_indices(s)
print(capitals)
