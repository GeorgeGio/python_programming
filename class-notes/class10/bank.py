

class Bank:

    bank_balance = 0




    def __init__(self,account_type):

        if account_type not in ["savings","checkings"]:

            raise TypeError("account_type should be savings or checkings")
        self.account_type = account_type
        self.balance = 0
        self.overdraft_fees = 0



    def deposit(self,deposit_amount):
        self.balance += deposit_amount
        Bank.bank_balance += deposit_amount


    def withdraw(self,withdraw_amount):
        self.balance -= withdraw_amount
        if self.balance <0:
            self.overdraft_fees += 20
        Bank.bank_balance -= withdraw_amount



account1= Bank("savings")
account1.deposit(20)
account1.withdraw(10)
account2 = Bank("checkings")
account2.deposit(1_000_000)
print(Bank.bank_balance)
account1.withdraw(100)
account1.withdraw(100)
print(account1.overdraft_fees)
