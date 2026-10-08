from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional
from pathlib import Path
import json
import time

app = FastAPI(
    title="Employee Management API",
    description="Basic to Intermediate HTTP Request Lifecycle Project",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

DATA_FILE = Path("employees.json")


class Employee(BaseModel):
    employee_name: str = Field(..., min_length=2)
    department: str = Field(..., min_length=2)
    job_role: str = Field(..., min_length=2)
    salary: float = Field(..., gt=0)
    city: str = Field(..., min_length=2)


class EmployeeUpdate(BaseModel):
    employee_name: Optional[str] = Field(None, min_length=2)
    department: Optional[str] = Field(None, min_length=2)
    job_role: Optional[str] = Field(None, min_length=2)
    salary: Optional[float] = Field(None, gt=0)
    city: Optional[str] = Field(None, min_length=2)


def load_employees():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_employees(employees):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(employees, file, indent=4)


@app.middleware("http")
async def request_logger(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time

    response.headers["X-Process-Time"] = str(round(process_time, 4))

    print(
        f"{request.method} {request.url.path} "
        f"-> {response.status_code} "
        f"({round(process_time, 4)} sec)"
    )

    return response


@app.get("/")
def home():
    return {
        "api_name": "Employee Management API",
        "status": "running",
        
    }


@app.get("/employees")
def get_employees(
    department: Optional[str] = Query(None),
    city: Optional[str] = Query(None)
):
    employees = load_employees()

    if department:
        employees = [
            employee
            for employee in employees
            if employee["department"].lower() == department.lower()
        ]

    if city:
        employees = [
            employee
            for employee in employees
            if employee["city"].lower() == city.lower()
        ]

    return {
        "count": len(employees),
        "employees": employees
    }


@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    employees = load_employees()

    for employee in employees:
        if employee["employee_id"] == employee_id:
            return employee

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )


@app.post("/employees", status_code=201)
def create_employee(employee: Employee):
    employees = load_employees()

    new_id = max(
        employee["employee_id"]
        for employee in employees
    ) + 1

    new_employee = {
        "employee_id": new_id,
        **employee.model_dump()
    }

    employees.append(new_employee)
    save_employees(employees)

    return {
        "message": "Employee created successfully",
        "employee": new_employee
    }


@app.put("/employees/{employee_id}")
def update_employee(
    employee_id: int,
    employee: Employee
):
    employees = load_employees()

    for index, existing_employee in enumerate(employees):
        if existing_employee["employee_id"] == employee_id:
            updated_employee = {
                "employee_id": employee_id,
                **employee.model_dump()
            }

            employees[index] = updated_employee
            save_employees(employees)

            return {
                "message": "Employee updated successfully",
                "employee": updated_employee
            }

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )


@app.patch("/employees/{employee_id}")
def patch_employee(
    employee_id: int,
    employee_update: EmployeeUpdate
):
    employees = load_employees()

    for employee in employees:
        if employee["employee_id"] == employee_id:
            update_data = employee_update.model_dump(
                exclude_unset=True
            )

            if not update_data:
                raise HTTPException(
                    status_code=400,
                    detail="No fields provided for update"
                )

            employee.update(update_data)
            save_employees(employees)

            return {
                "message": "Employee partially updated successfully",
                "employee": employee
            }

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )


@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    employees = load_employees()

    for index, employee in enumerate(employees):
        if employee["employee_id"] == employee_id:
            deleted_employee = employees.pop(index)
            save_employees(employees)

            return {
                "message": "Employee deleted successfully",
                "employee": deleted_employee
            }

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )


@app.get("/employees/statistics/summary")
def employee_statistics():
    employees = load_employees()

    total_employees = len(employees)

    total_salary = sum(
        employee["salary"]
        for employee in employees
    )

    average_salary = (
        total_salary / total_employees
        if total_employees > 0
        else 0
    )

    departments = {}

    for employee in employees:
        department = employee["department"]
        departments[department] = (
            departments.get(department, 0) + 1
        )

    return {
        "total_employees": total_employees,
        "average_salary": round(average_salary, 2),
        "employees_by_department": departments
    }