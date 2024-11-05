from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)
    def __str__(self):
        StrProduct = f'{self.name}', f'{self.weight}', f'{self.category}'
        return StrProduct

class Shop:
    __file_name = 'products.txt'
    def get_product(self):
        file = open(self.__file_name, 'r+')
        prod_str = file.read()
        file.close()
        return prod.str

    def add(self, *products):
        file_get = self.get_product()
        for i in products:
            if self.get_product().find(f'{i.name}, ')== -1:
                file = open(self.__file_name, 'a')
                file.write(f'{i}\n')
                file.close()
            else:
                print(f'Продукт {i.name} уже имеется')


shop1 = Shop()
product1 = Product('Apple1', 0.4,'Fruits')
product2 = Product('Apple', 0.3,'Fruits')
product3 = Product('Cucumber', 5.3,'Vegetables')
product4 = Product('Peach', 2, 'Fruits')
print(product2)
shop1.add(product1, product2, product3, product4, product2)
print(f'\n{shop1.get_product()}')