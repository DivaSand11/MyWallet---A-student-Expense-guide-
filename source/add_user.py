import sqlite3
import os
from datetime import datetime

# Database path
db_path = os.path.join(os.path.dirname(__file__), "..", "database", "myWallet.db")

connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# User Details
name = "Diva"
monthly_income = 20000
currency = "INR"
created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

cursor.execute("""
INSERT INTO Users(name, monthly_income, currency, created_at)
VALUES (?, ?, ?, ?)
""", (name, monthly_income, currency, created_at))

connection.commit()

print("User added successfully!")

connection.close()