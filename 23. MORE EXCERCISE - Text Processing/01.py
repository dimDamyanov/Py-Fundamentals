n = int(input())
for _ in range(n):
    line = input()
    name = line[line.find('@')+1:line.find('|')]
    age = line[line.find('#')+1:line.find('*')]
    print(f'{name} is {age} years old.')