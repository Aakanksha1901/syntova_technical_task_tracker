from fastapi import FastAPI, HTTPException, Query, Header
from pydantic import BaseModel, Field
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
import json


# CREATE FASTAPI APPLICATION
app = FastAPI(
    title="E-commerce REST API",
    description="JSON and REST API practice project",
    version="1.0"
)

# CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# LOAD JSON DATA

with open("data.json", "r") as file:
    orders = json.load(file)


# PYDANTIC MODEL
class Order(BaseModel):

    order_date: str
    product: str
    category: str
    quantity: int = Field(gt=0)
    price: float = Field(gt=0)


# PATCH MODEL
class OrderUpdate(BaseModel):

    order_date: Optional[str] = None
    product: Optional[str] = None
    category: Optional[str] = None
    quantity: Optional[int] = Field(
        default=None,
        gt=0
    )
    price: Optional[float] = Field(
        default=None,
        gt=0
    )


# HOME

@app.get("/")
def home():

    return {
        "message": "E-commerce REST API is running successfully"
    }


# GET - ALL ORDERS

@app.get("/orders")
def get_orders():

    return {
        "success": True,
        "count": len(orders),
        "data": orders
    }


# GET - FILTER / SEARCH / SORT / PAGINATION

@app.get("/orders/filter")
def filter_orders(
    category: Optional[str] = None,
    search: Optional[str] = None,
    sort: Optional[str] = None,
    page: int = Query(1, gt=0),
    limit: int = Query(10, gt=0),
    accept: Optional[str] = Header(default=None)
):

    result = orders.copy()


    # FILTER
    # Example:
    # orders- filter ny category = Electronics
    
    if category:

        result = [
            order
            for order in result
            if order["category"].lower() == category.lower()
        ]


    # SEARCH
    # Example:
    # /orders/filter?search=Laptop
    
    if search:

        result = [
            order
            for order in result
            if search.lower() in order["product"].lower()
        ]


    # SORT
    # Example:
    # /orders/filter?sort=price

    if sort == "price":

        result = sorted(
            result,
            key=lambda x: x["price"]
        )

    elif sort == "quantity":

        result = sorted(
            result,
            key=lambda x: x["quantity"]
        )

    elif sort:

        raise HTTPException(
            status_code=400,
            detail="Sort must be price or quantity"
        )


    # PAGINATION
    # Example:
    # /orders/filter?page=1&limit=2

    start = (page - 1) * limit
    end = start + limit

    paginated_data = result[start:end]


    return {
        "success": True,
        "page": page,
        "limit": limit,
        "total": len(result),
        "data": paginated_data
    }


# GET - SINGLE ORDER
# PATH PARAMETER
# IMPORTANT:
# This comes AFTER /orders/filter
@app.get("/orders/{order_id}")
def get_order(order_id: int):

    for order in orders:

        if order["id"] == order_id:

            return {
                "success": True,
                "data": order
            }

    raise HTTPException(
        status_code=404,
        detail="Order not found"
    )


# POST - CREATE ORDER
@app.post("/orders", status_code=201)
def create_order(order: Order):

    new_id = max(
        item["id"] for item in orders
    ) + 1

    new_order = {
        "id": new_id,
        **order.model_dump()
    }

    orders.append(new_order)

    return {
        "success": True,
        "message": "Order created successfully",
        "data": new_order
    }


# PUT - COMPLETE UPDATE
@app.put("/orders/{order_id}")
def update_order(
    order_id: int,
    order: Order
):

    for item in orders:

        if item["id"] == order_id:

            item["order_date"] = order.order_date
            item["product"] = order.product
            item["category"] = order.category
            item["quantity"] = order.quantity
            item["price"] = order.price

            return {
                "success": True,
                "message": "Order completely updated",
                "data": item
            }

    raise HTTPException(
        status_code=404,
        detail="Order not found"
    )


# PATCH - PARTIAL UPDATE

@app.patch("/orders/{order_id}")
def patch_order(
    order_id: int,
    order: OrderUpdate
):

    for item in orders:

        if item["id"] == order_id:

            update_data = order.model_dump(
                exclude_unset=True
            )

            item.update(update_data)

            return {
                "success": True,
                "message": "Order partially updated",
                "data": item
            }

    raise HTTPException(
        status_code=404,
        detail="Order not found"
    )


# DELETE - DELETE ORDER

@app.delete("/orders/{order_id}")
def delete_order(order_id: int):

    for order in orders:

        if order["id"] == order_id:

            orders.remove(order)

            return {
                "success": True,
                "message": "Order deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Order not found"
    )