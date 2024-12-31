class BankAccount:
    def __init__(self, name):
        self._balance = 0
        self.name = name

    def deposit(self, amount):
        self._balance += amount
    
    def withdraw(self, amount):
        self._balance -= amount

    def get_balance(self):
        return self._balance

    def __str__(self):
        return f"Name: {self.name} and Balance: Hidden"

#Example 8:Using Encapsulation    
kristina = BankAccount("Kristina")
kristina.deposit(100)
print(kristina)
print(kristina.get_balance())
kristina.withdraw(50)
kristina.deposit(400)
kristina.withdraw(100)
print(kristina.get_balance())
