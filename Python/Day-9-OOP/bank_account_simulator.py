class Account:
    def __init__( self, bal,acc):
        self.balance = bal
        self.account = acc
    
    def debit(self,amount):
        self.balance -= amount
        print("Rs.", amount, 'debited in your account')
        print("Total balance = " , self.get_balance())

    def credit(self,amount):
        self.balance += amount
        print("Rs.", amount, 'credited in your account')
        print("Total balance = " , self.get_balance())

    def get_balance(self):
        return self.balance
acc1 = Account(100000, 8156181)
acc1.debit(10000)
acc1.credit(1000)
