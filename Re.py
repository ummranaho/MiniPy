class Register:
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def register(self):
        print("User registered successfully!")

username=input("Enter username:")
password=input("Enter password:")
user=Register(username,password)
user.register()