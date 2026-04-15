class BankAccount:
    def __init__(self,name,balance,pin):
        self.name = name 
        self.__pin = pin
        self.history = []
        if balance <0:
            print("Initail balnce cannot be negative. setting it to 0")
            self.__balance = 0
        else:
            self.__balance = balance
        
    def __check_pin(self,pin):
        return self.__pin ==pin
    
    def deposit(self,amount,pin):
        if not self.__check_pin(pin):
            print("Incorrect pin")
            return
        if amount <=0:
            print("Invalid amount")
        else:
            self.__balance +=amount
            self.history.append(f"Deposited {amount}")
            print(f"{amount} deposited successfully.")

    def withdraw(self,amount,pin):
        if not self.__check_pin(pin):
            print("Invalid pin")
            return
        if amount <= 0:
            print("Invalid amount")
        elif self.__balance < amount:
            print("Insufficient Balance")
        else:
            self.__balance -= amount
            self.history.append(f"Withdraw {amount}")
            print(f"{amount} successfully withdraw.")        

    def show_balance(self,pin):
        if not self.__check_pin(pin):
            print("Invalid pin")
            return 
        print(f"Your current balance is: {self.__balance}")

    def transfer(self,amount,other_acc,pin):
        if not self.__check_pin(pin):
            print("Invalid pin")
            return 
        if amount < 0:
            print("Invalid amount")
        elif self.__balance < amount:
            print(f"We can't process your request as you have insufficient balance.")
        else:
            self.__balance -= amount
            other_acc.__balance += amount
            self.history.append(f"Transferred {amount} to {other_acc.name}")
            other_acc.history.append(f"Received {amount} from {self.name}")

            print(f"{amount} transferred from {self.name} to {other_acc.name}")

    def show_history(self):
        print(f"\nTransaction History for {self.name}:")
    
        if not self.history:
            print("No transactions yet.")
        else:
            for t in self.history:
                print(t)