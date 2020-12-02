words = input().split(', ')
text = input()
for word in words:
    text = text.replace(word, '*'*len(word), text.count(word))
print(text)