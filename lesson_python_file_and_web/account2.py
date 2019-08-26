class Account:
    """Bank account, which has balance as cents (1/100 euros)
    """
    def __init__(self, balance):
        self.balance = balance # public by default
    def __str__(self):
        return "Account(%d)" % self.balance

a = Account(500) # 5 euros
print(a)
a.balance += 1000 # add 10 euros
print(a)
# you can add new attributes / features to existing objects and classses
# however this is generally not recommended, as it makes it confusing for
# other programmers
a.type = "saving"
print(a.type)

        