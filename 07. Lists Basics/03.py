n = int(input())
negatives = []
positives = []
for i in range(n):
    num = int(input())
    positives.append(num) if num >= 0 else negatives.append(num)
print(positives, negatives, f'Count of positives: {len(positives)}. Sum of negatives: {sum(negatives)}', sep='\n')
