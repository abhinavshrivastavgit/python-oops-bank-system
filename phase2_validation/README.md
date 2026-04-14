# 🏦 Phase 2: Bank Account System with Validation

## 📌 Overview

In this phase, the Bank Account system is upgraded with **input validation and real-world constraints**.

Unlike Phase 1 (basic functionality), this phase ensures that **invalid or unsafe operations are blocked**, making the system more reliable and closer to real banking behavior.

---

## 🎯 Objectives

- Add **validation rules** to all operations
- Prevent invalid transactions
- Improve system robustness
- Learn **defensive programming**

---

## 🧠 Concepts Covered

| Concept               | Description                              |
| --------------------- | ---------------------------------------- |
| Validation            | Checking correctness of input            |
| Conditional Logic     | Using `if-elif-else` for decision making |
| Defensive Programming | Preventing misuse of system              |
| Improved OOP Design   | Making methods safer and smarter         |

---

## ⚙️ Features Implemented

- ✅ Prevent negative deposits
- ✅ Prevent zero-value deposits
- ✅ Prevent negative withdrawals
- ✅ Prevent withdrawing more than balance
- ✅ Prevent negative initial balance
- ✅ Clear user feedback messages

---

## 🧱 Project Structure

```id="7rqf1y"
Python-oops-bank-system/
│
├── phase2_validation/
│   ├── bank_account.py   # Updated class with validation
│   └── README.md
│
├── final_project_cli/
│   └── main.py           # Execution / testing
│
└── README.md
```

---

## 💻 Implementation

### 📁 `bank_account.py`

```python id="rql5pi"
class BankAccount:
    def __init__(self, name, balance):
        self.name = name

        if balance < 0:
            print("Initial balance cannot be negative. Setting it to 0.")
            self.balance = 0
        else:
            self.balance = balance

    def account_info(self):
        print(f"Account holder name is: {self.name}")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount. Deposit amount must be greater than 0.")
        else:
            self.balance += amount
            print(f"{amount} has been successfully deposited.")

    def withdraw(self, amount):
        if amount <= 0:
            print(f"Invalid amount {amount}, as amount should be more than 0.")
        elif self.balance < amount:
            print(f"Insufficient balance. Your current balance is {self.balance}")
        else:
            self.balance -= amount
            print(f"You have successfully withdrawn {amount}. Current balance: {self.balance}")

    def show_balance(self):
        print(f"Your Current Balance is {self.balance}")
```

---

## ▶️ How to Run

1. Navigate to project root:

   ```
   Python-oops-bank-system/
   ```

2. Run the program:

   ```
   python final_project_cli/main.py
   ```

---

## 🧪 Test Cases

Try these inputs to verify validation:

```python id="vrbcbb"
acc.deposit(-100)
acc.deposit(0)
acc.withdraw(-50)
acc.withdraw(999999)
```

Expected: All invalid operations should be rejected with proper messages.

---

## 🚫 Limitations (Phase 2)

- No transaction history tracking
- No transfer between accounts
- No security (PIN/password)
- Data is not fully encapsulated yet

---

## 🚀 Next Phase

➡️ **Phase 3: Transfer System**

- Transfer money between accounts
- Object-to-object interaction
- Deeper understanding of OOP

---

## 👨‍💻 Author

Abhinav Shrivastav

---

## ⭐ Key Takeaway

This phase introduces **real-world thinking in code**.
Instead of just making things work, we ensure:

> “The system behaves correctly even when the user makes mistakes.”

This is a critical step toward becoming a **backend developer**.
