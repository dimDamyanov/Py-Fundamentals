population = list(map(int, input().split(', ')))
min_wealth = int(input())
if min_wealth * len(population) > sum(population):
    print('No equal distribution possible')
else:
    for i in range(len(population)):
        if population[i] < min_wealth:
            population[population.index(max(population))] -= (min_wealth - population[i])
            population[i] = min_wealth
    print(population)