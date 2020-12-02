trace = list(map(int, input().split()))
left_racer = 0
right_racer = 0

for i in range(int((len(trace) - 1) / 2)):
    if trace[i] == 0:
        left_racer *= 0.8
    else:
        left_racer += trace[i]

    if trace[len(trace) - (i + 1)] == 0:
        right_racer *= 0.8
    else:
        right_racer += trace[len(trace) - (i + 1)]

if left_racer < right_racer:
    print(f'The winner is left with total time: {left_racer:.1f}')
else:
    print(f'The winner is right with total time: {right_racer:.1f}')