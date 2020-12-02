substrings = input().split(', ')
strings = input().split(', ')
contained = []

for string in strings:
    for substring in substrings:
        if substring in string and substring not in contained:
            contained.append(substring)

contained.sort(key=lambda x: substrings.index(x))
print(contained)