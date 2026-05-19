class Bank:
    def __init__(self, account_number, balance):
        self.__account_number=account_number
        self.__balance=balance
    
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
        return self.__balance

    def withdraw(self, amount):
        if amount<self.__balance:
            self.__balance-=amount
        return self.__balance
    
    def get_balance(self):
        return self.__balance

    
    def min_balance(self, min_amount):
        if self.__balance<min_amount:
            print("your account balance is less than minimum balance")
        return self.__balance
    
    
bank=Bank("12345", 6000)
bank_min_balance=Bank("13247", 400)

print(bank.deposit(3000))
print(bank.withdraw(2000))
print(bank_min_balance.min_balance(500))    
        


