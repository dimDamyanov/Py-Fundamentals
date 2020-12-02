n = int(input())
free_chairs = 0
enough_chairs = True
for i in range(n):
    data = input().split()
    if len(data[0]) >= int(data[1]):
        free_chairs += (len(data[0]) - int(data[1]))
    else:
        print(f'{int(data[1]) - len(data[0])} more chairs needed in room {(i + 1)}')
        enough_chairs = False

if enough_chairs:
    print(f'Game On, {free_chairs} free chairs left')