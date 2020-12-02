n = int(input())
grades = {}
for _ in range(n):
    name = input()
    grade = float(input())
    if name in grades:
        grades[name].append(grade)
    else:
        grades[name] = [grade]

for key in grades:
    grades[key] = sum(grades[key]) / len(grades[key])

grades = {k: v for k, v in grades.items() if v >= 4.5}
grades = sorted(grades.items(), key=lambda x: x[1], reverse=True)
for s, g in grades:
    print(f'{s} -> {g:.2f}')