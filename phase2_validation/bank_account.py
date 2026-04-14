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