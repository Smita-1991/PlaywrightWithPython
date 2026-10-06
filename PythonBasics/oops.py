class BankAccount:

    def __init__(self,account_holder_name,balance):
        self.account_holder_name = account_holder_name
        self.balance = balance

    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance-=amount

    def getBalance(self):
        return self.balance

account=BankAccount("John Doe", 1000)
account.deposit(500)
print(account.getBalance())

account.withdraw(200)
print(account.getBalance())