
sales = [12000, 0, 8500, 15000, -200, 9800]

total = 0
target = 30000

for x in sales:
    if x <= 0:
        print("Skipped invalid value", x)
        continue

    total += x
    print("Added", x, "total", total)

    if total > target:
        break

if total > target:
    print("Target reached. Stopped at", total)
elif total == target:
    print("Target reached exactly", total)
else:
    print("Target not reached")




      
prices = [500, 1200, 800, 2500, 300]

def apply_discount(price, discount=10):
    return round(price - (price * discount / 100), 2)

def total(*args):
    return sum(args)

def describe(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

above_1000 = [price for price in prices if price > 1000]

prices_with_gst = list(map(lambda price: round(price * 1.18, 2), prices))

below_1000 = list(filter(lambda price: price < 1000, prices))

print("Original prices:", prices)

print("Apply 10% discount:", apply_discount(1000))
print("Apply 20% discount:", apply_discount(1000, 20))

print("Total:", total(100, 200, 300))
print("Total of prices:", total(*prices))

print("Describe:")
describe(name="Praveen", role="Python Learner", level="Beginner")

print("Prices above 1000:", above_1000)

print("Prices with 18% GST:", prices_with_gst)

print("Prices below 1000:", below_1000)











class InsufficientFundsError(Exception):
    pass


class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} deposited {amount} -> balance {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Insufficient funds: balance {self.balance}, requested {amount}"
            )

        self.balance -= amount
        print(f"{self.owner} withdrew {amount} -> balance {self.balance}")

    def show(self):
        print(f"Owner: {self.owner}, Balance: {self.balance}")


account = Account("Arun", 1000)

try:
    account.deposit(500)
    account.withdraw(2000)

except InsufficientFundsError as e:
    print(f"Error: {e}")

finally:
    print("Transaction finished")









class InsufficientFundsError(Exception):
    pass


class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} deposited {amount} -> balance {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Insufficient funds: balance {self.balance}, requested {amount}"
            )

        self.balance -= amount
        print(f"{self.owner} withdrew {amount} -> balance {self.balance}")

    def show(self):
        print(f"Owner: {self.owner}, Balance: {self.balance}")


class SavingsAccount(Account):
    def __init__(self, owner, balance=0, min_balance=500):
        super().__init__(owner, balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            raise InsufficientFundsError(
                f"Insufficient funds: balance {self.balance}, requested {amount}"
            )

        self.balance -= amount
        print(f"{self.owner} withdrew {amount} -> balance {self.balance}")


priya = SavingsAccount("Priya", 1500)

try:
    priya.withdraw(1200)
except InsufficientFundsError as e:
    print(f"Error: {e}")

try:
    priya.withdraw(800)
except InsufficientFundsError as e:
    print(f"Error: {e}")

print(isinstance(priya, Account))
