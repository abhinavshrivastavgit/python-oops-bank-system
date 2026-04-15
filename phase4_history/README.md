# 🏦 Phase 4: Bank Account System with Transaction History

## 📌 Overview

In this phase, the banking system is enhanced with **transaction history tracking**.

Each account now maintains a record of all activities such as:

- Deposits
- Withdrawals
- Transfers (sent & received)

This introduces the concept of **state management and logging**, making the system behave more like a real-world banking application.

---

## 🎯 Objectives

- Store transaction history inside each account
- Track all operations performed on an account
- Display transaction logs to the user
- Understand how objects can maintain internal state over time

---

## 🧠 Concepts Covered

| Concept          | Description                          |
| ---------------- | ------------------------------------ |
| Lists            | Used to store transaction history    |
| State Management | Object remembers past actions        |
| Logging          | Recording system activity            |
| OOP Interaction  | Updating multiple objects (transfer) |

---

## ⚙️ Features Implemented

- ✅ Track deposits
- ✅ Track withdrawals
- ✅ Track transfers (both sender & receiver)
- ✅ Display full transaction history
- ✅ Handle empty history case

---

## 🧱 Project Structure

```id="7b98ra"
Python-oops-bank-system/
│
├── phase4_history/
│   ├── bank_account.py   # Class with transaction history
│   └── README.md
│
├── final_project_cli/
│   └── main.py           # Execution / testing
│
└── README.md
```

---

## 💻 Implementation

### 📁 `bank_account.py` (Key Additions)

```python id="8l94t1"
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.history = []   # 🧠 stores transactions

        if balance < 0:
            print("Initial balance cannot be negative. Setting it to 0.")
            self.balance = 0
        else:
            self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount.")
        else:
            self.balance += amount
            self.history.append(f"Deposited {amount}")
            print(f"{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount.")
        elif self.balance < amount:
            print("Insufficient balance.")
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
        print(f"\nTransaction History for {self.name}:")

        if not self.history:
            print("No transactions yet.")
        else:
            for transaction in self.history:
                print(transaction)
```

---

## ▶️ How to Run

1. Navigate to project root:

   ```
   Python-oops-bank-system/
   ```

2. Run:

   ```
   python final_project_cli/main.py
   ```

---

## 🧪 Example Usage

```python id="3nuh9h"
acc1 = BankAccount("Rahul", 5000)
acc2 = BankAccount("Priya", 2000)

acc1.deposit(1000)
acc1.withdraw(500)
acc1.transfer(700, acc2)

acc1.show_history()
acc2.show_history()
```

---

## 🧾 Sample Output

```id="c1hnwv"
Transaction History for Rahul:
Deposited 1000
Withdrew 500
Transferred 700 to Priya

Transaction History for Priya:
Received 700 from Rahul
```

---

## 🚫 Limitations (Phase 4)

- No timestamps in transactions
- No data persistence (history resets on restart)
- No security (PIN or access control)
- Balance is still publicly accessible

---

## 🚀 Next Phase

➡️ **Phase 5: Security & Encapsulation**

- Hide sensitive data (`__balance`, `__pin`)
- Add PIN-based authentication
- Restrict unauthorized access

---

## 👨‍💻 Author

Abhinav Shrivastav

---

## ⭐ Key Takeaway

This phase introduces the idea that:

> “A system should not only perform actions, but also remember them.”

This is a key step toward building **real-world applications with state and history tracking**.
