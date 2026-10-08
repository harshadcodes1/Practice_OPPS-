#Constructor in Python  

class BankAccount:

    # Constructor
    def __init__(self, name, account_no, balance):
        self.name = name
        self.account_no = account_no
        self.balance = balance

    # Display account details
    def display(self):
        print("\n--- Account Details ---")
        print("Name:", self.name)
        print("Account Number:", self.account_no)
        print("Balance:", self.balance)

    # Deposit money
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Amount deposited:", amount)
        print("New balance:", self.balance)

    # Withdraw money
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Amount withdrawn:", amount)
            print("Remaining balance:", self.balance)
        else:
            print("Insufficient balance")


# Creating object

name = input("Enter your name: ")
account_no = input("Enter account number: ")
balance = float(input("Enter initial balance: "))

account = BankAccount(name, account_no, balance)

while True:
    print("\n===== BANK MENU =====")
    print("1. Display Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        account.display()

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == 4:
        print("Thank you for using the Bank System!")
        break

    else:
        print("Invalid choice")