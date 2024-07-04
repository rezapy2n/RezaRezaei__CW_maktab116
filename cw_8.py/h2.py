class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot add money amounts with different currencies.")
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot subtract money amounts with different currencies.")
        return Money(self.amount - other.amount, self.currency)

    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency

    def __lt__(self, other):
        return self.amount < other.amount

    def __gt__(self, other):
        return self.amount > other.amount

    def display(self):
        return f"{self.currency} {self.amount:.2f}"


money1 = Money(100.50, "USD")
money2 = Money(75.20, "USD")

total_money = money1 + money2
print(f"Total money: {total_money.display()}")

print(f"Is money1 greater than money2? {money1 > money2}")
