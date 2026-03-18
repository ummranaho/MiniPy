class Salary:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def show_details(self):
            print(f"Employee Name: {self.name}\n Salary: {self.salary}")
    def increase_salary(self,emp):
        if emp==self.name:
            I_amount=(10/100)*self.salary
            new_salary=(self.salary + I_amount)
            print(f"Employee name: {self.name} \n Increased amount: {I_amount} \n new salary: {new_salary}" ) 
        else:
            print(f"There is no employee named {emp}")
 
S1=Salary("Bob",50000)

S1.show_details()
S1.increase_salary("Bob")