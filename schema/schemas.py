def individual_serial(emp) -> dict:
    return {
        "id": str(emp["_id"]),
        "name": emp["employee_name"],
        "phoneNo": emp["phoneNo"],
        "age": emp["age"],
    }


def list_serial(employees) -> list:
    return [individual_serial(emp) for emp in employees]