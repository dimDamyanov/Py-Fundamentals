import re
data = input()
dates = re.finditer(r'(?P<day>\d{2})(?P<sep>[./-])(?P<month>[A-Z][a-z]{2})(?P=sep)(?P<year>\d{4})', data)
for d in dates:
    print(f'Day: {d["day"]}, Month: {d["month"]}, Year: {d["year"]}')