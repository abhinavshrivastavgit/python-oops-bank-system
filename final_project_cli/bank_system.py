class BankSystem:
    def __init__(self):
        self.accounts ={}

    def create_account(self,name,balance,pin):
        if name in self.accounts:
            print("Account already exists.")
        else:
            from account import BankAccount
            self.accounts[name] = BankAccount(name,balance,pin)
            print(f"Account created for {name}")

    def get_account(self, name):
        return self.accounts.get(name)