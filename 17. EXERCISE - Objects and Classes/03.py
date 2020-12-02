class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        return [e for e in self.products if e[0] == first_letter]

    def __repr__(self):
        res = f'Items in the {self.name} catalogue:'
        for e in sorted(self.products):
            res += f'\n{e}'
        return res