class Mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def call(self):
        print(f"{self.brand} is making a call.")
m1= Mobile("Apple",999)
m1.call()

m2= Mobile("Samsung",799)
m2.call()
