from phase5_security.bank_account import BankAccount

acc1 = BankAccount("Rahul", 5000, 1234)
acc2 = BankAccount("Priya", 2000, 5678)

acc1.deposit(1000, 1234)
acc1.withdraw(500, 1234)

acc1.transfer(700, acc2, 1234)

acc1.show_balance(1234)
acc1.show_balance(9999)   # wrong PIN

acc1.show_history()
acc2.show_history()