class Company:
    def __init__(self, name, surname, position, salary, workhours):
        self.name = name
        self.surname = surname
        self.position = position
        self.salary = salary
        self.workhours = workhours

company1 = Company('John', 'Doe', 'Software Engineer', 80000, 'Full-time')
company2 = Company('Jane', 'Smith', 'Data Scientist', 95000, 'Full-time')
company3 = Company('Alice', 'Johnson', 'Product Manager', 90000, 'Part-time')
company4 = Company('Bob', 'Brown', 'UX Designer', 70000, 'Contract')
company5 = Company('Charlie', 'Davis', 'DevOps Engineer', 85000, 'Full-time')
company6 = Company('Eve', 'Wilson', 'QA Engineer', 60000, 'Full-time')
company7 = Company('Frank', 'Garcia', 'Systems Analyst', 75000, 'Part-time')
company8 = Company('Grace', 'Martinez', 'Network Engineer', 80000, 'Contract')
company9 = Company('Hank', 'Lopez', 'Database Administrator', 90000, 'Full-time')
company10 = Company('Ivy', 'Gonzalez', 'Security Analyst', 95000, 'Full-time')

print(company1.name)
print(company2.surname)
print(company3.position)
print(company4.salary)
print(company5.workhours)
print(company6.name)
print(company7.surname)
print(company8.position)
print(company9.salary)
print(company10.workhours)