encrypted_words = input().split()
message = []
for encrypted_word in encrypted_words:
    num = int(''.join([c for c in encrypted_word if c.isdigit()]))
    word = list(chr(num) + ''.join([c for c in encrypted_word if c.isalpha()]))
    word[1], word[len(word) - 1] = word[len(word) - 1], word[1]
    message.append(''.join(word))

print(*message, sep=' ')