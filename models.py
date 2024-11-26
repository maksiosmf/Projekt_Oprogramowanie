from pydantic import BaseModel
from typing import List, Optional

class Product(BaseModel):
    id: int
    name: str
    price: float

    def update_price(self, new_price: float):
        self.price = new_price


class Category(BaseModel):
    id: int
    name: str
    products: List[Product] = []

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product_id: int):
        self.products = [product for product in self.products if product.id != product_id]
