line = input().split()
searched = input()

palindromes = []
for word in line:
    if word == word[::-1]:
        palindromes.append(word)

print(palindromes)
print(f'Found palindrome {palindromes.count(searched)} times')