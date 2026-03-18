class Employee:

    def __init__(self, name, salary):
        # Defining Properties
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Emplyee Name: {self.name}")
        print(f"Employee Salary: {self.salary}")

        # print(f" Employee Name: {self.name} \n Employee Salary: {self.salary}")

    def increase_salary(self):
        increased_amount = (10/100) * self.salary
        new_salary = self.salary + increased_amount
        print(f"Emplyee Name: {self.name}")
        print(f"Increased Salary: {increased_amount}")
        print(f"New Salay: {new_salary}")
# Defining an Object
E1 = Employee("Jenny", 80000)
E1.show_details()
E1.increase_salary()