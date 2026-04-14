from phase1_basic.bank_account import BankAccount

#Create an account
acc1 = BankAccount("Rahul",1000)

#Performing Actions
acc1.account_info()
acc1.deposit(5000)
acc1.showBalance()
acc1.withdraw(550)
acc1.showBalance()
