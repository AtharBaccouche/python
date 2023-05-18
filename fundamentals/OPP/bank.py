class BankAccount:
    accounts=[]
    def __init__(self, int_rate, balance): 
        self.int_rate=int_rate 
        self.balance=balance
        BankAccount.accounts.append(self)
    def deposit(self, amount):
        self.balance +=amount
        return self
    
    def withdraw(self, amount):
        if(self.balance-amount)>=0:
            self.balance-=amount
        else:
            print("Insufficient funds: changing a $5 fee")
            self.balance-=5
        return self
    def display_account_info(self):
        print(f"Blance:{self.balance}")
        return(self)
    def yield_interest(self):
        if self.balance>0:
            self.balance+=(self.balance*self.int_rate)
        return self
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            print(f"Balance: {account.balance} \n interest rate : {account.int_rate}")



account1=BankAccount(.05,2000)
account2=BankAccount(.03, 5000)


account1.deposit(300).deposit(200).deposit(100).withdraw(70).display_account_info()
account2.deposit(300).deposit(200).withdraw(100).withdraw(70).withdraw(20).withdraw(30).display_account_info().yield_interest()
print("=================================")
BankAccount.print_all_accounts()
print("=================================================")
class User:
    def __init__(self,user_first_name,user_last_name,user_email,user_age):
        self.first_name = user_first_name
        self.last_name = user_last_name
        self.email = user_email
        self.age = user_age
        self.account= BankAccount(0.02,500)
    
    def display_info_user(self):
        print(f"Name: {self.first_name} {self.last_name}\n Email: {self.email}\n Age:{self.age}\n with balance = {self.account.balance}")
    def make_deposite(self,amount):
        self.account.deposit(amount)
        print(f"{self.first_name} has an account with balance ={self.account.balance}")
    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        print(f"{self.first_name} has an account with balance ={self.account.balance}")
    def display_user_balance(self):
        self.account.display_account_info(self)

user1=User("Asma","Baccouche","asma@live.fr",25)
user1.display_info_user()
user1.make_deposite(1000)
user1.make_withdraw(200)

