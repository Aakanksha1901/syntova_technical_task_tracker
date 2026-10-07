from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


# HOME

def test_home():

    response = client.get("/")

    assert response.status_code == 200


# GET ALL ORDERS
def test_get_orders():

    response = client.get("/orders")

    assert response.status_code == 200


# GET SINGLE ORDER
def test_get_order():

    response = client.get("/orders/1")

    assert response.status_code == 200


# GET NOT FOUND
def test_order_not_found():

    response = client.get("/orders/999")

    assert response.status_code == 404


# POST
def test_create_order():

    response = client.post(
        "/orders",
        json={
            "order_date": "2026-02-10",
            "product": "Tablet",
            "category": "Electronics",
            "quantity": 2,
            "price": 30000
        }
    )

    assert response.status_code == 201


# POST VALIDATION
def test_invalid_order():

    response = client.post(
        "/orders",
        json={
            "order_date": "2026-02-10",
            "product": "Tablet",
            "category": "Electronics",
            "quantity": -2,
            "price": 30000
        }
    )

    assert response.status_code == 422


# PUT
def test_put_order():

    response = client.put(
        "/orders/1",
        json={
            "order_date": "2026-02-15",
            "product": "Gaming Laptop",
            "category": "Electronics",
            "quantity": 3,
            "price": 75000
        }
    )

    assert response.status_code == 200


# PATCH
def test_patch_order():

    response = client.patch(
        "/orders/1",
        json={
            "price": 70000
        }
    )

    assert response.status_code == 200


# DELETE
def test_delete_order():

    response = client.delete("/orders/5")

    assert response.status_code == 200


#  FILTER

def test_filter():

    response = client.get(
        "/orders/filter?category=Electronics"
    )

    assert response.status_code == 200


# SEARCH
def test_search():

    response = client.get(
        "/orders/filter?search=Laptop"
    )

    assert response.status_code == 200


# SORT
def test_sort():

    response = client.get(
        "/orders/filter?sort=price"
    )

    assert response.status_code == 200


# PAGINATION

def test_pagination():

    response = client.get(
        "/orders/filter?page=1&limit=2"
    )

    assert response.status_code == 200