from fastapi import APIRouter, HTTPException
from typing import List
from ..models import Product

router = APIRouter(prefix="/products", tags=["Products"])

products = [
    Product(id=1, name="Laptop", price=1200.00),
    Product(id=2, name="Myszka", price=25.00),
    Product(id=3, name="Klawiatura", price=50.00),
    Product(id=4, name="Słuchawki", price=60.00),
]

@router.post("/", response_model=Product)
def create_product(product: Product):
    products.append(product)
    return product

@router.get("/{product_id}", response_model=Product)
def get_product(product_id: int):
    product = next((p for p in products if p.id == product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/{product_id}", response_model=Product)
def update_product(product_id: int, updated_product: Product):
    product = next((p for p in products if p.id == product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    product.name = updated_product.name
    product.price = updated_product.price
    return product

@router.delete("/{product_id}", response_model=dict)
def delete_product(product_id: int):
    global products
    products = [p for p in products if p.id != product_id]
    return {"detail": "Product deleted"}
