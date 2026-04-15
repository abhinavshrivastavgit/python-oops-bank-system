from phase4_history.bank_account import BankAccount

acc1 = BankAccount("Rahul", 5000)
acc2 = BankAccount("Priya", 2000)

acc1.deposit(1000)
acc1.withdraw(500)
acc1.transfer(700, acc2)

acc1.show_history()
acc2.show_history()