sub = input()
string = input()
while sub in string:
    string = string.replace(sub, '')
print(string)