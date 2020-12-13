s = input()
line = input()
while line != 'Finish':
    tokens = line.split()
    if tokens[0] == 'Replace':
        s = s.replace(tokens[1], tokens[2])
        print(s)
    elif tokens[0] == 'Cut':
        start_ind = int(tokens[1])
        end_ind = int(tokens[2])
        if len(s) > start_ind >= 0 and len(s) > end_ind >= 0:
            s = s[:start_ind] + s[end_ind+1:]
            print(s)
        else:
            print('Invalid indices!')
    elif tokens[0] == 'Make':
        if tokens[1] == 'Upper':
            s = s.upper()
            print(s)
        elif tokens[1] == 'Lower':
            s = s.lower()
            print(s)
    elif tokens[0] == 'Check':
        if tokens[1] in s:
            print(f'Message contains {tokens[1]}')
        else:
            print(f"Message doesn't contain {tokens[1]}")
    elif tokens[0] == 'Sum':
        start_ind = int(tokens[1])
        end_ind = int(tokens[2])
        if len(s) > start_ind >= 0 and len(s) > end_ind >= 0:
            sub = s[start_ind:end_ind+1]
            print(sum([ord(c) for c in sub]))
        else:
            print('Invalid indices!')
    line = input()