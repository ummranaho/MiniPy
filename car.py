class Car:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year
    def drive(self):
        print(f"{self.brand} is driving.")
c1= Car("Toyota",2022)
c1.drive()
