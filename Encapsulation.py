# Encapsulation : Bank Account Managment

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance       

    
    def get_balance(self):
        print("Current Balance:", self.__balance)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount Deposited:", amount)
        else:
            print("Invalid Amount")

    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print("Amount Withdrawn:", amount)
        else:
            print("Insufficient Balance")


# Creating object
account = BankAccount("Harshad", 10000)

print("Account Holder:", account.name)

account.get_balance()

account.deposit(5000)
account.get_balance()

account.withdraw(3000)
account.get_balance()