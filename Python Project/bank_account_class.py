# Program to create a simple BankAccount class

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    # The deposit method denotes money is deposited
    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    # The method to withdraw money
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)

    # The method to show balance
    def display_balance(self):
        print("Current balance:", self.balance)


# Created object and test
acc = BankAccount()

acc.deposit(16000)
acc.withdraw(5000)
acc.display_balance()
