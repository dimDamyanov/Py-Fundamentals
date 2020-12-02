data = input().split()
queries = input().split()
bakery = {}
for i in range(0, len(data), 2):
    bakery[data[i]] = int(data[i+1])
for q in queries:
    if q in bakery:
        print(f'We have {bakery[q]} of {q} left')
    else:
        print(f'Sorry, we don\'t have {q}')