def print_employee_data(name: str, born_in: int, today: int):
    print(f"Name: {name}")
    print(f"Age: {today-born_in}")

def calculate_age(born_in: int, today: int):
    return born_in - today

print_employee_data("John Doe", 1967, 2022)
print_employee_data("Jack Doe", 1958,2022)
print_employee_data("Jane Doe", 1997, 2022)

print(calculate_age(2010,2022))
result = calculate_age(2022,1920)
print(f"A gyerek {result} éves")


