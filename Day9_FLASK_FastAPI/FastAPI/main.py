#import libraries
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()


# PYDANTIC MODELS

class Product(BaseModel):
    name: str
    category: str
    price: float = Field(..., gt=0)
    quantity: int = Field(..., ge=0)


class ProductResponse(BaseModel):
    name: str
    category: str
    price: float
    quantity: int


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    price: Optional[float] = Field(None, gt=0)
    quantity: Optional[int] = Field(None, ge=0)


# PRODUCT DATA

products = {
    1: {
        "name": "Laptop",
        "category": "Electronics",
        "price": 55000,
        "quantity": 10
    },
    2: {
        "name": "Mouse",
        "category": "Electronics",
        "price": 800,
        "quantity": 25
    },
    3: {
        "name": "Running Shoes",
        "category": "Footwear",
        "price": 2500,
        "quantity": 15
    }
}


# 1. HOME API

@app.get("/")
def home():
    return {
        "message": "E-Commerce API is working!"
    }


# 2. GET PRODUCT

@app.get(
    "/products/{product_id}",
    response_model=ProductResponse
)
def get_product(product_id: int):

    if product_id not in products:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return products[product_id]


# 3. SEARCH PRODUCTS

@app.get("/search")
def search_products(category: str):

    results = []

    for product in products.values():

        if product["category"].lower() == category.lower():
            results.append(product)

    return results


# 4. ADD PRODUCT

@app.post("/products")
def add_product(product: Product):

    new_id = max(products.keys()) + 1

    products[new_id] = product.model_dump()

    return {
        "message": "Product added successfully",
        "product_id": new_id,
        "product": products[new_id]
    }


# 5. UPDATE PRODUCT - PUT

@app.put("/products/{product_id}")
def update_product(
    product_id: int,
    product: Product
):

    if product_id not in products:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    products[product_id] = product.model_dump()

    return {
        "message": "Product updated successfully",
        "product_id": product_id,
        "product": products[product_id]
    }


# 6. DELETE PRODUCT

@app.delete("/products/{product_id}")
def delete_product(product_id: int):

    if product_id not in products:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    deleted_product = products.pop(product_id)

    return {
        "message": "Product deleted successfully",
        "product_id": product_id,
        "product": deleted_product
    }


# 7. PATCH PRODUCT

@app.patch("/products/{product_id}")
def patch_product(
    product_id: int,
    product: ProductUpdate
):

    if product_id not in products:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    update_data = product.model_dump(
        exclude_unset=True
    )

    products[product_id].update(update_data)

    return {
        "message": "Product partially updated",
        "product_id": product_id,
        "product": products[product_id]
    }