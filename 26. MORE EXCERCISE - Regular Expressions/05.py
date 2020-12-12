import re

title = ''
content = []
pattern = r'(?P<tag>[a-z.="]+)>(\\[\w])?(?P<text>[\w\s]+)<'
line = input()
data = re.finditer(pattern, line)
for e in data:
    if e['tag'] == 'title':
        title = e['text']
    elif e['tag'] == 'Content2':
        content.append('Body2')
    else:
        content.append(e['text'])
print(f'Title: {title}')
print(f'Content: {"".join(content)}')