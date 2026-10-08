import json

import pytest
from fastapi.testclient import TestClient

import app


TEST_EMPLOYEES = [
    {
        "employee_id": 1,
        "employee_name": "Aarav Sharma",
        "department": "IT",
        "job_role": "Python Developer",
        "salary": 55000,
        "city": "Pune"
    },
    {
        "employee_id": 2,
        "employee_name": "Priya Patil",
        "department": "HR",
        "job_role": "HR Executive",
        "salary": 48000,
        "city": "Kolhapur"
    },
    {
        "employee_id": 3,
        "employee_name": "Rohan Deshmukh",
        "department": "Finance",
        "job_role": "Financial Analyst",
        "salary": 62000,
        "city": "Mumbai"
    }
]


@pytest.fixture
def client(tmp_path, monkeypatch):
    test_file = tmp_path / "employees.json"

    with open(test_file, "w", encoding="utf-8") as file:
        json.dump(TEST_EMPLOYEES, file, indent=4)

    monkeypatch.setattr(app, "DATA_FILE", test_file)

    return TestClient(app.app)


def test_home(client):
    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["api_name"] == "Employee Management API"
    assert data["status"] == "running"


def test_get_all_employees(client):
    response = client.get("/employees")

    assert response.status_code == 200

    data = response.json()

    assert data["count"] == 3
    assert len(data["employees"]) == 3


def test_get_employee(client):
    response = client.get("/employees/1")

    assert response.status_code == 200
    assert response.json()["employee_id"] == 1


def test_employee_not_found(client):
    response = client.get("/employees/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Employee not found"


def test_filter_by_department(client):
    response = client.get("/employees?department=IT")

    assert response.status_code == 200

    data = response.json()

    assert data["count"] == 1
    assert data["employees"][0]["department"] == "IT"


def test_filter_by_city(client):
    response = client.get("/employees?city=Pune")

    assert response.status_code == 200

    data = response.json()

    assert data["count"] == 1
    assert data["employees"][0]["city"] == "Pune"


def test_create_employee(client):
    new_employee = {
        "employee_name": "Sneha Kulkarni",
        "department": "IT",
        "job_role": "Data Analyst",
        "salary": 58000,
        "city": "Pune"
    }

    response = client.post(
        "/employees",
        json=new_employee
    )

    assert response.status_code == 201

    data = response.json()

    assert data["employee"]["employee_name"] == "Sneha Kulkarni"


def test_invalid_employee(client):
    invalid_employee = {
        "employee_name": "A",
        "department": "IT",
        "job_role": "Developer",
        "salary": -100,
        "city": "Pune"
    }

    response = client.post(
        "/employees",
        json=invalid_employee
    )

    assert response.status_code == 422


def test_update_employee(client):
    updated_employee = {
        "employee_name": "Aarav Updated",
        "department": "IT",
        "job_role": "Senior Python Developer",
        "salary": 70000,
        "city": "Mumbai"
    }

    response = client.put(
        "/employees/1",
        json=updated_employee
    )

    assert response.status_code == 200
    assert response.json()["employee"]["salary"] == 70000


def test_patch_employee(client):
    response = client.patch(
        "/employees/1",
        json={
            "salary": 65000
        }
    )

    assert response.status_code == 200
    assert response.json()["employee"]["salary"] == 65000


def test_delete_employee(client):
    response = client.delete("/employees/1")

    assert response.status_code == 200
    assert response.json()["message"] == "Employee deleted successfully"


def test_statistics(client):
    response = client.get("/employees/statistics/summary")

    assert response.status_code == 200

    data = response.json()

    assert data["total_employees"] == 3
    assert "average_salary" in data
    assert "employees_by_department" in data


def test_process_time_header(client):
    response = client.get("/")

    assert response.status_code == 200
    assert "X-Process-Time" in response.headers