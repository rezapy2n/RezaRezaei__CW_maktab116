class BankAccount:
    def __init__(self, account_number, initial_balance):
        self._account_number = account_number  
        self._balance = initial_balance  

    # Getter method for balance
    def get_balance(self):
        return self._balance

    
    def set_balance(self, new_balance):
        if new_balance >= 0:
            self._balance = new_balance
        else:
            print("Invalid balance. Please provide a non-negative value.")


my_account = BankAccount(account_number="123456", initial_balance=1000)


print(f"Initial balance: {my_account.get_balance()}")


my_account.set_balance(1500)

print(f"Updated balance: {my_account.get_balance()}")
