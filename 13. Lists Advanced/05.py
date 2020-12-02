happiness = list(map(int, input().split()))
factor = int(input())
emp = len(happiness)
happiness = [e * factor for e in happiness]
avg = sum(happiness) / len(happiness)
happiness = [e for e in happiness if e >= avg]
if len(happiness) >= emp / 2:
    print(f'Score: {len(happiness)}/{emp}. Employees are happy!')
else:
    print(f'Score: {len(happiness)}/{emp}. Employees are not happy!')
