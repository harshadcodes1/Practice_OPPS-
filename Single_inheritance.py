# Single Inheritance : Bank account Managment

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def display_account(self):
        print("Name:", self.name)
        print("Balance:", self.balance)


class SavingsAccount(BankAccount):

    def add_interest(self):
        interest = self.balance * 0.05
        self.balance = self.balance + interest
        print("Interest Added:", interest)
        print("New Balance:", self.balance)


account = SavingsAccount("Harshad", 10000)

account.display_account()
account.add_interest()