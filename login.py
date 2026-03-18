class Login:
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def authenticate(self):
        if(self.username =="admin"and self.password=="admin123"):
            print("Login successful")
        else:
            print("Invalid username or password")

username=input("Enter username:")
password=input("Enter password:")
user = Login(username,password)
user.authenticate()



