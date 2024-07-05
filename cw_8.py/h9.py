import random


class BankAccount:

    def __init__(self,account_number,balance) -> None:
        self.__account_number = account_number
        self.__balance = balance

    @property
    def account_number(self):
        return self.__account_number
    
    @account_number.setter
    def account_number(self,value):
        self.__account_number = value

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self,value):
        if value > 10000:
            self.__balance = value
        else:
            print('error')

    def display(self):
        return f'account number: {self.__account_number}\naccount balance: {self.__balance}'


# poya_password = random.randint(100000,1000000)

# print(poya_password)

a1 = BankAccount(481632,100000)



print(a1.display())