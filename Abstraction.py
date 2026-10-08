# Abstraction concept in python 


from abc import ABC, abstractmethod

class Bank(ABC):

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass


class SBI(Bank):

    def withdraw(self, amount):
        print("Withdraw ₹", amount, "from SBI account")

    def deposit(self, amount):
        print("Deposit ₹", amount, "into SBI account")


account = SBI()

account.withdraw(2000)
account.deposit(5000)