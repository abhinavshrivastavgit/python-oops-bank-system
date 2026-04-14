class BankAccount:
    def __init__(self, name, balance):
        self.name = name

        if balance < 0:
            print("Initial balance cannot be negative. Setting it to 0.")
            self.balance = 0
        else:
            self.balance = balance

    def account_info(self):
        print(f"Account holder name is: {self.name}")

    def deposit(self,amount):
        if amount<=0:
            print("Invalid amount.Deposit amount must be greater than Zero'0' ")
        else:
            self.balance+=amount
            print(f"{amount} has been successfully deposited.")

    
    def withdraw(self,amount):
        if amount<=0:
            print(f"Invalid amount {amount}, as amount should be more than Zero.")

        else:
            if self.balance<amount:
                print(f"You have entered the invalid amount: {amount} as your account balance is {self.balance}")
            else:
                self.balance-=amount
                print(f"You have successfully withdrawn amount {amount}, Now your current balance is: {self.balance}")

    def show_balance(self):
        print(f"Your Current Balance is {self.balance}")

    def transfer(self,amount,other_account):
        if self == other_account:
            print("Cannot transfer to the same account.")
        elif amount<=0:
            print(f"Enter amount {amount} is invalid. Transfer amount must be greater than Zero.")
        elif self.balance < amount:
                print(f"We can't process your request as your available balance is low.\nYour Balance: {self.balance} and Your Request: {amount}")
        else:
                self.balance-= amount
                other_account.balance+=amount
                print(f"{amount} transferred from {self.name} to {other_account.name}")