import os
import sqlite3

# Database Path
db_path = os.path.join(os.path.dirname(__file__), "myWallet.db")

# Connect to Database
connection = sqlite3.connect(db_path)

# Create Cursor
cursor = connection.cursor()

print("Connected to MyWallet Database!")

# -----------------------------
# USERS TABLE
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    monthly_income REAL NOT NULL,
    currency TEXT NOT NULL,
    created_at TEXT NOT NULL
)
""")

# -----------------------------
# CATEGORIES TABLE
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS Categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT NOT NULL,
    icon TEXT,
    is_default INTEGER DEFAULT 1
)
""")

# -----------------------------
# EXPENSES TABLE
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS Expenses (
    expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    amount REAL NOT NULL,
    description TEXT,
    payment_method TEXT,
    expense_date TEXT NOT NULL,
    created_at TEXT NOT NULL,

    FOREIGN KEY(user_id) REFERENCES Users(user_id),
    FOREIGN KEY(category_id) REFERENCES Categories(category_id)
)
""")

# -----------------------------
# INCOME TABLE
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS Income (
    income_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    source TEXT NOT NULL,
    amount REAL NOT NULL,
    income_date TEXT NOT NULL,
    notes TEXT,

    FOREIGN KEY(user_id) REFERENCES Users(user_id)
)
""")

# -----------------------------
# BUDGET TABLE
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS Budget (
    budget_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    month INTEGER NOT NULL,
    year INTEGER NOT NULL,
    allocated_budget REAL NOT NULL,

    FOREIGN KEY(user_id) REFERENCES Users(user_id),
    FOREIGN KEY(category_id) REFERENCES Categories(category_id)
)
""")

# -----------------------------
# SAVINGS GOALS TABLE
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS SavingsGoals (
    goal_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    goal_name TEXT NOT NULL,
    target_amount REAL NOT NULL,
    deadline TEXT,

    FOREIGN KEY(user_id) REFERENCES Users(user_id)
)
""")

# Save Changes
connection.commit()

print("All tables created successfully!")

# Close Connection
connection.close()

print("Database setup completed!")