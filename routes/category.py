from fastapi import APIRouter, HTTPException
from typing import List
from ..models import Category, Product

router = APIRouter(prefix="/categories", tags=["Categories"])

categories = [
    Category(id=1, name="Electronics", products=[]),
]

@router.post("/", response_model=Category)
def create_category(category: Category):
    categories.append(category)
    return category

@router.get("/{category_id}", response_model=Category)
def get_category(category_id: int):
    category = next((c for c in categories if c.id == category_id), None)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.put("/{category_id}", response_model=Category)
def update_category(category_id: int, updated_category: Category):
    category = next((c for c in categories if c.id == category_id), None)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    category.name = updated_category.name
    category.products = updated_category.products
    return category

@router.delete("/{category_id}", response_model=dict)
def delete_category(category_id: int):
    global categories
    categories = [c for c in categories if c.id != category_id]
    return {"detail": "Category deleted"}
