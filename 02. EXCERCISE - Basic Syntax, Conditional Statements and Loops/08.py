input_string = input()
output_string = input()
s = input_string

for i in range(len(input_string)):
    s1 = input_string[(i + 1):]
    s2 = output_string[:(i + 1)]
    if s2 + s1 == s:
        continue
    s = s2 + s1
    print(s)
