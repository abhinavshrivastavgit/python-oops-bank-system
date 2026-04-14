# 🏦 Phase 1: Basic Bank Account System

## 📌 Overview

This phase focuses on building the **foundation** of a Bank Account system using Object-Oriented Programming (OOP) in Python.

We implement a simple `BankAccount` class that allows basic banking operations like:

- Creating an account
- Depositing money
- Withdrawing money
- Checking account balance

---

## 🎯 Objectives

- Understand **Classes and Objects**
- Learn how to use the `__init__` constructor
- Implement **methods (functions inside class)**
- Build a clean separation between **logic and execution**

---

## 🧱 Project Structure

```
Python-oops-bank-system/
│
├── phase1_basic/
│   ├── bank_account.py   # Core class (logic)
│   └── README.md
│
├── final_project_cli/
│   └── main.py           # Execution / testing
│
└── README.md
```

---

## 🧠 Concepts Covered

| Concept       | Description                        |
| ------------- | ---------------------------------- |
| Class         | Blueprint for Bank Account         |
| Object        | Instance of a class (real account) |
| Constructor   | `__init__` to initialize data      |
| Methods       | Actions like deposit/withdraw      |
| Encapsulation | Binding data + methods together    |

---

## ⚙️ Features Implemented

- ✅ Create a bank account
- ✅ Deposit money
- ✅ Withdraw money (with balance check)
- ✅ Display current balance
- ✅ Show account holder info

---

## 💻 Code Example

### 📁 `bank_account.py`

```python
class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def account_info(self):
        print(f"Account holder name is: {self.name}")

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} successfully deposited.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} has been successfully withdrawn from your account.")
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print(f"Your Current Balance is {self.balance}")
```

---

### 📁 `test.py`

```python
from phase1_basic.bank_account import BankAccount

acc1 = BankAccount("Rahul", 1000)

acc1.account_info()
acc1.deposit(5000)
acc1.show_balance()

acc1.withdraw(550)
acc1.show_balance()
```

---

## ▶️ How to Run

1. Open terminal in root folder:

   ```
   Python-oops-bank-system/
   ```

2. Run the program:

   ```
   python final_project_cli/main.py
   ```

---

## 🧪 Sample Output

```
Account holder name is: Rahul
5000 successfully deposited.
Your Current Balance is 6000
550 has been successfully withdrawn from your account.
Your Current Balance is 5450
```

---

## 🚫 Limitations (Phase 1)

- No input validation (handled in Phase 2)
- No transaction history
- No security (PIN/password)

---

## 🚀 Next Phase

➡️ **Phase 2: Validation**

- Prevent negative deposits
- Prevent invalid withdrawals
- Improve robustness of system

---

## 👨‍💻 Author

Abhinav Shrivastav

---

## ⭐ Key Takeaway

This phase builds the **core foundation of OOP**.
A strong understanding here makes advanced features much easier in later phases.
