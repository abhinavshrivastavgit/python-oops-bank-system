class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance  #data
    
    def account_info(self):
        print(f"Account holder name is: {self.name}")
    #action1
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance -= amount
            print(f"{amount} has been successfully withdrawn from your account.")
        else:
            print("Insufficient Balance")
    
    #action2
    def deposit(self,amount):
        self.balance +=amount
        print(f"{amount} successfully deposited.")


    #action3
    def showBalance(self):
        print(f"Your Current Balance is {self.balance}")





