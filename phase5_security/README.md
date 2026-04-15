# 🔐 Phase 5: Secure Bank Account System (Encapsulation)

## 📌 Overview

In this phase, the banking system is upgraded with **security and encapsulation**.

Sensitive data such as account balance and PIN are now **hidden (private)** and can only be accessed through controlled methods. This makes the system safer and closer to real-world banking applications.

---

## 🎯 Objectives

- Protect sensitive data using encapsulation
- Implement PIN-based authentication
- Restrict unauthorized access to account operations
- Enforce controlled interaction with account data

---

## 🧠 Concepts Covered

| Concept           | Description                             |
| ----------------- | --------------------------------------- |
| Encapsulation     | Hiding internal data from direct access |
| Private Variables | Using `__` to restrict access           |
| Access Control    | Allowing operations only via methods    |
| Authentication    | Verifying user identity using PIN       |

---

## ⚙️ Features Implemented

- ✅ Private balance (`__balance`)
- ✅ Private PIN (`__pin`)
- ✅ PIN verification before transactions
- ✅ Secure deposit and withdrawal
- ✅ Protected balance access
- ✅ Secure transfer between accounts
- ✅ Transaction history maintained

---

## 🧱 Project Structure

```id="s9z0jk"
Python-oops-bank-system/
│
├── phase5_security/
│   ├── bank_account.py   # Secure class with encapsulation
│   └── README.md
│
├── final_project_cli/
│   └── main.py           # Execution / testing
│
└── README.md
```

---

## 💻 Implementation

### 📁 `bank_account.py` (Key Highlights)

```python id="cuvkqb"
class BankAccount:
    def __init__(self, name, balance, pin):
        self.name = name
        self.__pin = pin
        self.history = []

        if balance < 0:
            print("Initial balance cannot be negative. Setting it to 0.")
            self.__balance = 0
        else:
            self.__balance = balance

    def __check_pin(self, pin):
        return self.__pin == pin

    def deposit(self, amount, pin):
        if not self.__check_pin(pin):
            print("Incorrect PIN")
            return

        if amount <= 0:
            print("Invalid amount.")
        else:
            self.__balance += amount
            self.history.append(f"Deposited {amount}")
            print(f"{amount} deposited successfully.")

    def withdraw(self, amount, pin):
        if not self.__check_pin(pin):
            print("Incorrect PIN")
            return

        if amount <= 0:
            print("Invalid amount.")
        elif self.__balance < amount:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            self.history.append(f"Withdrew {amount}")
            print(f"{amount} withdrawn successfully.")

    def transfer(self, amount, other_account, pin):
        if not self.__check_pin(pin):
            print("Incorrect PIN")
            return

        if self == other_account:
            print("Cannot transfer to same account.")
        elif amount <= 0:
            print("Invalid amount.")
        elif self.__balance < amount:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            other_account.__balance += amount

            self.history.append(f"Transferred {amount} to {other_account.name}")
            other_account.history.append(f"Received {amount} from {self.name}")

            print(f"{amount} transferred from {self.name} to {other_account.name}")

    def show_balance(self, pin):
        if not self.__check_pin(pin):
            print("Incorrect PIN")
            return

        print(f"Your Balance is {self.__balance}")

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

2. Run the program:

   ```
   python final_project_cli/main.py
   ```

---

## 🧪 Example Usage

```python id="3kcdgc"
acc1 = BankAccount("Rahul", 5000, 1234)
acc2 = BankAccount("Priya", 2000, 5678)

acc1.deposit(1000, 1234)
acc1.withdraw(500, 1234)
acc1.transfer(700, acc2, 1234)

acc1.show_balance(1234)
acc1.show_history()
```

---

## 🔐 Security Features

- Balance is **not directly accessible**
- PIN is **hidden and verified internally**
- Unauthorized access is blocked
- All operations require authentication

---

## 🚫 Limitations

- PIN is stored in plain form (not encrypted)
- No account lock after multiple wrong attempts
- No persistent storage (data resets on restart)

---

## 🚀 Next Steps (Future Enhancements)

- Add PIN encryption
- Add login system
- Save data using files or database
- Convert to API using Flask/FastAPI
- Build frontend interface

---

## 👨‍💻 Author

Abhinav Shrivastav

---

## ⭐ Key Takeaway

This phase completes the transformation from:

> “Basic program” → “Secure system”

Encapsulation ensures that:

> “Data is protected and only accessed in a controlled way.”

This is a core principle used in **real-world backend systems and software engineering**.
