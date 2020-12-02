import re

line = input()
data = ''
total = 0
pattern = r'>>(?P<item>[a-z]+)<<(?P<price>\d+(\.\d+)*)!(?P<quantity>\d+)'
while line != 'Purchase':
    data += f'\n{line}'
    line = input()
i_dicts = [i.groupdict() for i in
           re.finditer(r'>>(?P<item>[a-z]+)<<(?P<price>\d+(\.\d+)*)!(?P<quantity>\d+)', data, re.IGNORECASE)]
print('Bought furniture:')
for item in i_dicts:
    print(f'{item["item"]}')
    total += float(item['price']) * int(item['quantity'])
print(f'Total money spend: {total:.2f}')
