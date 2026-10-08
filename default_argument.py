def create_account(name, balance=1000):
    print("\n--- Account Details ---")
    print("Name:", name)
    print("Initial Balance:", balance)


def deposit(balance, amount=500):
    balance = balance + amount
    print("Deposited Amount:", amount)
    print("New Balance:", balance)
    return balance


def withdraw(balance, amount=200):
    if amount <= balance:
        balance = balance - amount
        print("Withdrawn Amount:", amount)
        print("Remaining Balance:", balance)
    else:
        print("Insufficient Balance")

    return balance


# Main Program

name = input("Enter your name: ")

create_account(name)

balance = 1000

print("\n1. Deposit")
print("2. Withdraw")

choice = int(input("Enter your choice: "))

if choice == 1:
    amount = int(input("Enter amount (Enter 0 for default ₹500): "))

    if amount == 0:
        balance = deposit(balance)
    else:
        balance = deposit(balance, amount)

elif choice == 2:
    amount = int(input("Enter amount (Enter 0 for default ₹200): "))

    if amount == 0:
        balance = withdraw(balance)
    else:
        balance = withdraw(balance, amount)

else:
    print("Invalid Choice")