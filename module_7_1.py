class Product:
    def __init__(self, name='', weight=0.0, category=''):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        products_have = (open(self.__file_name, 'r')).read()
        open(self.__file_name, 'r').close()
        return products_have

    def add(self, *products):
        for prd in products:
            if self.get_products().find(str(prd.name)) >= 0:
                print(f'Продукт {prd.name} уже есть в магазине')
                continue
            else:
                open(self.__file_name, 'a').write(str(prd) + '\n')
                open(self.__file_name, 'a').close()
        return


s1 = Shop()
p1 = Product('Potato',    50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4,  'Groceries')
p3 = Product('Potato',    5.5,  'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
