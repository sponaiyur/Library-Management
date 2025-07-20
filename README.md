# 📚 Library-Management System
This was a simple project undertaken during senior-secondary school, to understand the real world impact of python programming. The system makes use of Python as the frontend (UI programmed using the Tkinter module) and MySQL as the backend.

---

## Features ✨
- 👩‍🎓 Has two types of access control - Student and Librarian
- 💻 Automatic password generation based on student name (first three letters of the student + @2023)
- 📕 Borrowing/Returning of books made simple using the dynamic Treeview layout
- 👩‍💻 Admin access includes creating a student account, adding books, viewing overdue books

---

## 🖥️ Installation and System Requirements
Please ensure your current python version supports tkinter, an in-built graphics module.

But first things first, Install MySQL, if not already present:
- [MySQL download for Windows](https://dev.mysql.com/downloads/installer/)

Or, install via package manager:
```bash
sudo apt install mysql-server       # Ubuntu/Debian
brew install mysql                  # macOS with Homebrew
```

- proceed with the application installation:
```bash 
#1. Clone the repository
git clone https://github.com/sponaiyur/Library-Management
cd Library-Management

#2. Activate virtual environment (optional, skip if you're using a global setup)
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

#3. Install dependencies
pip install -r requirements.txt

#4. Run the initial database schema into your personal MySQL database
python init_db.py #or simply execute the python file in your system

#5. RUn the application
python main_prg.py
```
### Note: This application does not make use of .env to hold database credentials, and instead makes use of '*****' and '^^^^^' placeholders to hard-code the values. It is highly recommended to create a .env file, and modify the code accordingly to securely handle sensitive credentials.

---

## 🚀 Usage
The usage is pretty straightforward, run the application and interact with the UI. An Admin account has been created by default, and it is recommended to "create" new user accounts through the UI for better experience. Some book records have been added into the system, but the current UI does not support deleting books through the interface. Hence, the user is expected to modify the `schema.sql` file to directly remove books they don't prefer.

---

## 🛡️License
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

This project is licensed under the [MIT License](LICENSE).

Feel free to use, modify and share — with proper attribution. 

---

## 🙋‍♀️ Contributions
Pull requests are welcome! For major changes, please open an issue first.





