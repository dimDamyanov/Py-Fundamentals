n = int(input())
syn_dict = {}
for i in range(n):
    key = input()
    value = input()
    if key in syn_dict:
        syn_dict[key].append(value)
    else:
        syn_dict[key] = [value]

for key, value in syn_dict.items():
    print(f'{key} - {", ".join(value)}')