class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def show_product(self):
        print(f"Product Name: {self.name}\n Price: {self.price}\n Quantity: {self.quantity}")

    def sell(self,amount):
        if amount<=self.quantity:
            self.quantity-=amount
            print(f"Sold {amount} units of {self.name}. Remaining quantity: {self.quantity}")
        else:
            print(f"Insufficient quantity of {self.name}. Available: {self.quantity}")
p1=Product("Laptop",1200,50)
p1.show_product()
p1.sell(20)