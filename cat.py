class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def meow(self):
        return f"{self.name} says meow!"
    
    def meow_p(self):
        print(f"{self.name} says meow!")

c1= Cat("kitty",2)
print(c1.meow())
c1.meow_p()
# print(c1.name)
    