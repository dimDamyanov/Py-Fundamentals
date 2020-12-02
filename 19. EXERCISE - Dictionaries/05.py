parking = {}
n = int(input())
for _ in range(n):
    data = input().split()
    if data[0] == 'register':
        if data[1] in parking:
            print(f'ERROR: already registered with plate number {parking[data[1]]}')
        else:
            parking[data[1]] = data[2]
            print(f'{data[1]} registered {parking[data[1]]} successfully')
    elif data[0] == 'unregister':
        if data[1] in parking:
            parking.pop(data[1])
            print(f'{data[1]} unregistered successfully')
        else:
            print(f'ERROR: user {data[1]} not found')

for key, value in parking.items():
    print(f'{key} => {value}')