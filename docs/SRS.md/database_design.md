# Database Design

# Project Name

MyWallet

Version: 1.0

---

# 1. Overview

The MyWallet application uses a relational database to securely store and manage user financial information. The database is designed to organize data efficiently while minimizing redundancy and ensuring consistency.

SQLite has been selected as the database management system because it is lightweight, serverless, easy to integrate with Python, and ideal for single-user desktop applications.

The database stores user information, income records, expenses, budgets, savings goals, and expense categories.

---

# 2. Database Type

Database Management System (DBMS)

SQLite

Database Model

Relational Database

Storage

Local Storage

Programming Language

Python

---

# 3. Database Objectives

The database is designed to:

- Store all financial information securely.
- Organize expenses efficiently.
- Track multiple income sources.
- Maintain category-wise budgets.
- Monitor savings goals.
- Support monthly financial analytics.
- Allow future expansion without redesigning the database.

---

# 4. Database Tables

The database consists of the following tables:

1. Users
2. Categories
3. Expenses
4. Income
5. Budgets
6. Savings

Each table has a unique purpose and is connected through relationships.

---

# 5. Table Details

## 5.1 Users

Purpose

Stores information about the application user.

Columns

- user_id (Primary Key)
- name
- monthly_income
- currency
- created_at

Description

There will initially be only one user, but the database is designed to support multiple users in future versions.

---

## 5.2 Categories

Purpose

Stores all expense categories.

Examples

- Food
- Travel
- Education
- Shopping
- Entertainment
- Health
- Recharge
- Others

Custom categories created by users will also be stored here.

Columns

- category_id (Primary Key)
- category_name
- icon
- is_default

---

## 5.3 Expenses

Purpose

Stores every expense made by the user.

Columns

- expense_id (Primary Key)
- user_id (Foreign Key)
- category_id (Foreign Key)
- amount
- description
- payment_method
- expense_date
- created_at

Example

Amount : ₹350

Category : Food

Description : Pizza

Payment Method : UPI

Date : 26 June 2026

---

## 5.4 Income

Purpose

Stores all income entries.

Examples

- Pocket Money
- Internship
- Scholarship
- Freelancing
- Gifts

Columns

- income_id (Primary Key)
- user_id (Foreign Key)
- source
- amount
- income_date
- notes

---

## 5.5 Budgets

Purpose

Stores monthly budgets allocated for each expense category.

Columns

- budget_id (Primary Key)
- user_id (Foreign Key)
- category_id (Foreign Key)
- month
- year
- allocated_budget

Example

Food

₹3500

Travel

₹1000

Education

₹1800

---

## 5.6 Savings

Purpose

Stores the user's savings goals and current progress.

Columns

- saving_id (Primary Key)
- user_id (Foreign Key)
- goal_name
- goal_amount
- current_amount
- deadline

Example

Goal

Emergency Fund

Goal Amount

₹50,000

Current Savings

₹18,000

---

# 6. Relationships

The following relationships exist between the tables.

One User can have multiple Expenses.

One User can have multiple Income entries.

One User can have multiple Budget records.

One User can have multiple Savings goals.

One Category can contain multiple Expenses.

One Category can have one Budget allocation per month.

These relationships allow efficient querying and future scalability.

---

# 7. Primary Keys

Users

user_id

Categories

category_id

Expenses

expense_id

Income

income_id

Budgets

budget_id

Savings

saving_id

Each primary key uniquely identifies a record inside its respective table.

---

# 8. Foreign Keys

Expenses.user_id → Users.user_id

Expenses.category_id → Categories.category_id

Income.user_id → Users.user_id

Budgets.user_id → Users.user_id

Budgets.category_id → Categories.category_id

Savings.user_id → Users.user_id

Foreign keys establish relationships between tables and maintain referential integrity.

---

# 9. Data Flow

The following sequence describes how data moves through the application.

User

↓

Adds Income

↓

Income Table

↓

Dashboard Updated

↓

User Adds Expense

↓

Expense Stored

↓

Category Updated

↓

Budget Recalculated

↓

Analytics Updated

↓

Savings Updated

---

# 10. Normalization

The database follows normalization principles by storing related information in separate tables.

Benefits

- Reduced duplicate data
- Improved consistency
- Easier maintenance
- Better scalability
- Faster querying

---

# 11. Future Database Expansion

The current database has been designed so that future features can be added without major structural changes.

Possible future tables include:

- Investments
- Notifications
- Bank Accounts
- Transactions
- Bill Reminders
- AI Recommendations
- User Authentication
- Cloud Synchronization

---

# 12. Database Summary

Database

SQLite

Number of Tables

6

Primary Keys

6

Foreign Keys

6

Storage Type

Relational Database

Designed For

Offline Personal Finance Management

Scalability

High