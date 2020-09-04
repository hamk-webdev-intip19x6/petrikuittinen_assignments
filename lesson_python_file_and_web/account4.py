class Account:
    """Bank account, which has balance as cents (1/100 euros)"""
    # slots leads to less memory and CPU cycle usage, and you can limit
    # the future dynamic options
    __slots__ = ('balance', )  # tuple, which defines all attributes

    def __init__(self, balance):
        self.balance = balance  # public by default

    def deposit(self, amount):
        """deposit amount cents to account. Return current balance"""
        self.balance += amount
        return self.balance

    def draw(self, amount):
        """draw amount of cents from account. Return current balance"""
        # make sure balance doesn't go below zero
        self.balance = max(self.balance - amount, 0)
        return self.balance

    def __str__(self):
        return "Account(%d)" % self.balance


a = Account(500)  # 5 euros
b = Account(1000)  # 10 euros
print(a)
a.deposit(1000)  # add 10 euros
print(a)
a.draw(300)
print(a)
print(b.draw(100))
print(b.draw(9999999))
print(b.deposit(750))
# the following will work, because balance is public!
a.balance = 10**6
print(a)
