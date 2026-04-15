from bank_system import BankSystem

def main():
    bank = BankSystem()

    while True:
        print("\n===== BANK MENU =====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Show Balance")
        print("6. Show History")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            balance = int(input("Enter initial balance: "))
            pin = int(input("Set PIN: "))
            bank.create_account(name, balance, pin)

        elif choice == "2":
            name = input("Enter name: ")
            amount = int(input("Enter amount: "))
            pin = int(input("Enter PIN: "))
            acc = bank.get_account(name)
            if acc:
                acc.deposit(amount, pin)
            else:
                print("Account not found")

        elif choice == "3":
            name = input("Enter name: ")
            amount = int(input("Enter amount: "))
            pin = int(input("Enter PIN: "))

            acc = bank.get_account(name)
            if acc:
                acc.withdraw(amount, pin)
            else:
                print("Account not found")

        elif choice == "4":
            sender = input("Sender name: ")
            receiver = input("Receiver name: ")
            amount = int(input("Enter amount: "))
            pin = int(input("Enter PIN: "))

            acc1 = bank.get_account(sender)
            acc2 = bank.get_account(receiver)

            if acc1 and acc2:
                acc1.transfer(amount, acc2, pin)
            else:
                print("Invalid accounts")

        elif choice == "5":
            name = input("Enter name: ")
            pin = int(input("Enter PIN: "))

            acc = bank.get_account(name)
            if acc:
                acc.show_balance(pin)
            else:
                print("Account not found")

        elif choice == "6":
            name = input("Enter name: ")

            acc = bank.get_account(name)
            if acc:
                acc.show_history()
            else:
                print("Account not found")

        elif choice == "7":
            print("Thank you for using the bank system.")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()