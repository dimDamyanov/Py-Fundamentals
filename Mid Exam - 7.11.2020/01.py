n = int(input())
daily = int(input())
expected = float(input())
plunder = 0
for i in range(n):
    plunder += daily
    if (i + 1) % 3 == 0:
        plunder += 0.5 * daily
    if (i + 1) % 5 == 0:
        plunder *= 0.7

if plunder >= expected:
    print(f'Ahoy! {plunder:.2f} plunder gained.')
else:
    print(f'Collected only {((plunder / expected) * 100):.2f}% of the plunder.')
