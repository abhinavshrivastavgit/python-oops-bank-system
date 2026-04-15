# 🏦 Bank System CLI (Python OOP Project)

## 📌 Overview

A fully functional **Command-Line Banking System** built using Python and Object-Oriented Programming (OOP).

This project simulates real-world banking operations with:

- Multiple user accounts
- Secure transactions using PIN authentication
- Transaction history tracking
- Clean modular architecture

---

## 🚀 Features

- 👤 Create multiple bank accounts
- 💰 Deposit money (with validation)
- 💸 Withdraw money (with balance checks)
- 🔁 Transfer money between accounts
- 🔐 Secure access using PIN authentication
- 📜 Transaction history tracking
- 🧠 Encapsulation for data protection
- 🖥️ Interactive CLI-based interface

---

## 🧠 Concepts Used

| Concept          | Implementation                                  |
| ---------------- | ----------------------------------------------- |
| OOP              | Classes & Objects (`BankAccount`, `BankSystem`) |
| Encapsulation    | Private variables (`__balance`, `__pin`)        |
| Validation       | Input checks for safe transactions              |
| Data Structures  | Dictionary for account storage                  |
| State Management | Transaction history tracking                    |
| Modular Design   | Separate files for logic & interface            |

---

## 🏗️ Project Structure

```id="cli_struct"
final_project_cli/
│
├── account.py        # Core BankAccount class (logic + security)
├── bank_system.py    # Manages multiple accounts
├── main.py           # CLI interface (user interaction)
└── README.md
```

---

## ⚙️ How It Works

### 🔁 System Flow

```id="flow_struct"
User Input → CLI (main.py)
        ↓
BankSystem (manage accounts)
        ↓
BankAccount (business logic + security)
        ↓
Output to user
```

---

## ▶️ How to Run

1. Navigate to the folder:

   ```
   cd final_project_cli
   ```

2. Run the application:

   ```
   python main.py
   ```

---

## 💻 Sample Menu

```id="menu_sample"
===== BANK MENU =====
1. Create Account
2. Deposit
3. Withdraw
4. Transfer
5. Show Balance
6. Show History
7. Exit
```

---

## 🧪 Example Usage

```id="example_usage"
Create Account → Rahul, 5000, PIN: 1234
Deposit → 1000
Withdraw → 500
Transfer → Rahul → Priya → 700
```

---

## 🔐 Security Features

- Balance is **not directly accessible**
- PIN verification required for all transactions
- Private attributes ensure data protection
- Prevents invalid and unauthorized operations

---

## 📜 Transaction History

Each account maintains a log of:

- Deposits
- Withdrawals
- Transfers (sent & received)

---

## 🚫 Limitations

- Data is not persistent (resets on restart)
- PIN is stored in plain text
- No account deletion/update feature

---

## 🚀 Future Improvements

- 💾 Add file/database storage
- 🔒 Encrypt PINs
- 🌐 Convert to REST API (Flask/FastAPI)
- 🎨 Build frontend UI
- 🔑 Add login system

---

## 👨‍💻 Author

Abhinav Shrivastav

---

## ⭐ Key Takeaway

This project demonstrates how to build a **real-world system step-by-step** using OOP:

> From basic classes → to a secure, multi-user banking application.

---

## 🔗 Related Work

This project is part of a structured learning journey:

- Phase 1 → Basic OOP
- Phase 2 → Validation
- Phase 3 → Transfer Logic
- Phase 4 → Transaction History
- Phase 5 → Security & Encapsulation

---

## 💡 Final Thought

> “Instead of building multiple small projects, this system was evolved step-by-step into a complete application.”

---
