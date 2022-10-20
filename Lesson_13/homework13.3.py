class Product:
    def __init__(self, type: str, name: str, price: float, discount: float = 0.0) -> None:
        self.type = type
        self.name = name
        self.price = price
        self.discount = discount
    
    def __str__(self) -> str:
        return f"{self.type}, {self.name}, ${self.price}, {self.discount}% "
    
    def __repr__(self) -> str:
        return f"{self.type}, {self.name}, ${self.price}, {self.discount}% "

    

class ProductStore:
    def __init__(self, products: dict = {}, income: float = 0) -> None:
        self.products = products
        self.income = income
    
    def add(self, product: Product, amount: int):
        if product in self.products:
            self.products[product] += amount
        else:
            self.products[product] = amount

    def set_discount(self, identifier: str, percent: float, identifier_type: str = 'name'):
        if identifier_type == 'name':
            for product in self.products:
                if product.name == identifier:
                    product.discount = percent
        elif identifier_type == 'type':
            for product in self.products:
                if product.name == identifier:
                    product.discount = percent
        else: 
            raise ValueError

    def sell_product(self, product_name: str, amount: int):
        for product in self.products:
            if product_name == product.name:
                if self.products[product] >= amount:
                    self.products[product] -= amount
                    self.income += product.price * amount*(100-product.discount)/100.0
                else:
                    raise ValueError

    def get_income(self):
        return self.income

    def get_all_products(self):
        return self.products

    def get_product_info(self, product_name: str):
        return [(product.name, self.products[product]) for product in self.products if product.name == product_name]
       

p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.sell_product('Ramen', 10)
print(s.products[p])
s.add(p, 10)
print(s.products[p])
s.set_discount('Ramen', 50.0, 'name')
print(p2.discount)
s.sell_product('Ramen', 10)
print(s.products[p2])
print(s.get_income())
print(s.get_all_products())
print(s.get_product_info('Ramen'))

assert s.get_product_info('Ramen') == [('Ramen', 280)]