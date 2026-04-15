class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        if balance < 0:
            self.balance = 0
        else:
            self.balance = balance
        self.history = []

    def deposit(self,amount):
        if amount <=0:
            print(f"You have entered the inavlid amount: {amount}")
        
        else:
            self.balance += amount
            self.history.append(f"Deposited {amount}")
            print(f"{amount} deposited successfully")

    def withdraw(self,amount):
        if amount<=0:
             print(f"You have entered the inavlid amount: {amount}")
        elif self.balance<amount:
            print(f"You have entered more amount: {amount} than your balance: {self.balance}")

        else:
            self.balance -= amount
            self.history.append(f"Withdrew {amount}")
            print(f"{amount} withdrawn successfully.")

    def transfer(self, amount, other_account):
        if self == other_account:
            print("Cannot transfer to same account.")
    
        elif amount <= 0:
            print("Invalid amount.")
    
        elif self.balance < amount:
            print("Insufficient balance.")
    
        else:
            self.balance -= amount
            other_account.balance += amount

            self.history.append(f"Transferred {amount} to {other_account.name}")
            other_account.history.append(f"Received {amount} from {self.name}")

            print(f"{amount} transferred from {self.name} to {other_account.name}")
        
    def show_history(self):
        print(f"\nTransaction History for {self.name}")

        if not self.history:
            print("No Transaction yet")

        else:
            for transaction in self.history:
                print(transaction)