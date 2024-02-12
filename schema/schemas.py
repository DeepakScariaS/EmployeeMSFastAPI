def individual_serial(emp) -> dict:
    return {
        "id": str(emp["_id"]),
        "name": emp["name"],
        "age": emp["age"],
        "phoneNo": emp["phoneNo"]
    }


def list_serial(employees) -> list:
    return [individual_serial(emp) for emp in employees]
