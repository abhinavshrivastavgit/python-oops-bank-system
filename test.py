from phase3_transfer.bank_account import BankAccount

acc1 = BankAccount("Rahul", 5000)
acc2 = BankAccount("Priya", 2000)


acc1.show_balance()
acc2.show_balance()

acc1.transfer(1000, acc2)

acc1.show_balance()
acc2.show_balance()