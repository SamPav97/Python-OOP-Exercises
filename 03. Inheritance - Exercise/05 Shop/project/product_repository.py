
from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for prod in self.products:
            if prod.name == product_name:
                return prod

    def remove(self, product_name):
        product = self.find(product_name)
        if product is not None:
            self.products.remove(product)

    def __repr__(self):
        res = ""
        for prod in self.products:
            res += f"{prod.name}: {prod.quantity}\n"
        return res.strip()
