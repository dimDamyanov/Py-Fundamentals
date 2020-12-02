class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        result = ''
        if species == 'mammal':
            result += f'Mammals in {self.name}: {", ".join([str(e) for e in self.mammals])}'
        elif species == 'fish':
            result += f'Fishes in {self.name}: {", ".join([str(e) for e in self.fishes])}'
        elif species == 'bird':
            result += f'Birds in {self.name}: {", ".join([str(e) for e in self.birds])}'
        result += f'\nTotal animals: {Zoo.__animals}'
        return result


name = input()
zoo = Zoo(name)
n = int(input())
for i in range(n):
    data = input().split()
    zoo.add_animal(data[0], data[1])
print(zoo.get_info(input()))