class BankAccount:

    def __init__(self, accountBalance = 0):
        self.accountBalance = accountBalance

    def depositeMoney(self, amount):
        self.accountBalance += amount
        return self.accountBalance

    def withdrawMoney(self, amount):
        self.accountBalance -= amount
        return self.accountBalance

acc_1 = BankAccount()

print(acc_1.depositeMoney(1500))
print(acc_1.withdrawMoney(200))