n = int(input())
s = input()
strings = []
containing_strings = []
for i in range(n):
    line = input()
    strings.append(line)
    if s in line:
        containing_strings.append(line)
print(strings, containing_strings, sep='\n')
