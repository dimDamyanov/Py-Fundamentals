import re

name_pattern = r'(?<=%)[A-Z][a-z]+(?=%)'
product_pattern = r'(?<=<)\w+(?=>)'
count_pattern = r'(?<=\|)\d+(?=\|)'
price_pattern = r'\d+(\.[\d]+)?(?=\$)'
line = input()
total = 0
while line != 'end of shift':
    name = re.search(name_pattern, line)
    product = re.search(product_pattern, line)
    count = re.search(count_pattern, line)
    price = re.search(price_pattern, line)
    if name and product and count and price:
        count = int(count.group())
        price = float(price.group())
        total += price * count
        print(f'{name.group()}: {product.group()} - {(price * count):.2f}')
    line = input()
print(f'Total income: {total:.2f}')