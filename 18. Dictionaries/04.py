words = input().casefold().split()
words_count = {}
for w in words:
    words_count[w] = words.count(w)
odd = [e for e in words_count if words_count[e] % 2 != 0]
print(*odd, sep=' ')