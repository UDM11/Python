class Account:
    def __init__(self, balance, account_number):
        self.balance = balance
        self.account_number = account_number

    def debit(self, amount):
        self.balance -= amount
        print("RS. ", amount, "Was debited")
        print("Total balance =", self.balance)

    def credit(self, amount):
        self.balance += amount
        print("RS. ", amount, "Was credited")
        print("Total balance =", self.balance)

    def get_balance(self):
        return self.balance

account1 = Account(1000, 1234567890)
account1.debit(100)
account1.credit(200)