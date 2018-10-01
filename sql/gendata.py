#!/usr/bin/env python
"""Random people data generation for sqlite"""

import random

import faker


# Departments PK limits
DEP_MIN = 1
DEP_MAX = 20

# Employes PK limits
PERS_MIN = 1
PERS_MAX = 200

# Salary limits
SAL_MIN = 12000
SAL_MAX = 150000


fake = faker.Faker()


# Departments
cities = [fake.city() for _ in range(DEP_MIN, DEP_MAX + 1)]
for city in cities:
    print(f"INSERT INTO department(name) VALUES('{city}');")

# Employees
persons = [fake.name() for _ in range(PERS_MIN, PERS_MAX + 1)]
for i, person in enumerate(persons, 1):
    department_id = random.randint(DEP_MIN, DEP_MAX)
    chief_id = random.randint(PERS_MIN, i)
    name = fake.name()
    salary = random.randint(SAL_MIN, SAL_MAX)

    print(f"INSERT INTO employee(department_id, chief_id, name, salary)"
          f"VALUES({department_id}, {chief_id}, '{name}', {salary});")

