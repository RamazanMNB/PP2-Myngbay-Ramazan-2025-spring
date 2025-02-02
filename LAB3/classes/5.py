class bankacc:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print("deposited " + str(amount) + ". New balance: "+ str(self.balance))
        else:
            print("deposit -")
    def withdraw(self,amount):
        if amount <=self.balance:
            self.balance-=amount
            print("- " + str(amount) +  ". New balance: "+ str(self.balance))
    def get_balance(self):
        return self.balance
    
acc = bankacc("Ramazan Myngbay",200000)

print(acc.get_balance())

acc.deposit(20000)
acc.deposit(30000)

acc.withdraw(20000)
acc.withdraw(16000)

print(acc.get_balance())

        