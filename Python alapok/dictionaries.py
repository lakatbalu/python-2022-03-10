#dictionary, dict
#szótár
#kulcs-érték pár
# módosítható

employee = {"name": "john doe", "age": 40}

print(employee["name"])

employee2 = {5 : "john doe", 6: 40}

print(employee2[6])

for data in employee:
    print(data)

for key, value in employee.items():
    print(f"{key} --- {value}")

employee["age"] = 41
print(employee)

employee["color:of_eye"] ="blue"
print(employee)

employee["skills"] = ("java", "python", "c#")
print(employee)

print(employee["skills"][1])

salaries = {"2021-01": 100_000, "2021-02": 100_010, "2021-03": 150_000}

employee["salaries"] = salaries
print(employee)
print(employee["salaries"]["2021-03"])
