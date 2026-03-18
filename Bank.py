class BankAccount:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            self.balance += amount
            print("Deposit successful.")
            print(" New balance:", self.balance)
        else:
            print("Invalid amount")


    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient  Balance.")
        elif amount <= 0:
            print("Invalid amount.")
        else:
            self.balance -= amount
            print("Withdrew successfully.")
            print("Remaining balance:", self.balance)
    def display(self):
        print("\nAccount Details:")
        print("\Account Number:", self.account_number)
        print("Account Holder:", self.name)
        print("Balance:", self.balance)
accounts = {}

while True:
    print("\n===== Bank System =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print ("4.Balance check")
    print("5. Display Account Info")
    print("6. Exit")

    choice = input("Enter your choice : ")
    if choice == "1":
        account_number = input("Enter account number: ")
        name = input("Enter account holder's name: ")
        balance = float(input("Enter initial balance: "))
        account = BankAccount (account_number, name, balance)
        accounts[account_number] = account
        print("Account created successfully.")
    elif choice == "2":
        account_number = input("Enter account number: ")
        if account_number in accounts:
            amount = float(input("Enter amount to deposit: "))
            accounts[account_number].deposit(amount)
        else:
            print("Account not found.")
    elif choice == "3":
        account_number = input("Enter account number: ")
        if account_number in accounts:
            amount = float(input("Enter amount to withdraw: "))
            accounts[account_number].withdraw(amount)
        else:
            print("Account not found.")
    elif choice == "4":
        account_number = input("Enter account number: ")
        if account_number in accounts:
            print("Current balance:", accounts[account_number].balance)
        else:
            print("Account not found.")
    elif choice == "5":
        account_number = input("Enter account number: ")
        if account_number in accounts:
            accounts[account_number].display()
        else:
            print("Account not found.")
    elif choice == "6":
        print("Thankyou for using the Bank System .")
        break
    else:
        print("Invalid choice. Please try again.")
               

              