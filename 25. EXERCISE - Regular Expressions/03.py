import re
data = input()
word = input()
occurrences = len(re.findall(f'(^|(?<=\s)){word}([?!.,])*($|(?=\s))', data, re.IGNORECASE))
print(occurrences)