employee_list = []

n = int(input("Enter number of employees: "))

for i in range(n):
    name = input("Enter name: ")
    salary = int(input("Enter salary: "))
    employee_list.append((name, salary))

employee_dictionary = dict(employee_list)

print(employee_dictionary)



