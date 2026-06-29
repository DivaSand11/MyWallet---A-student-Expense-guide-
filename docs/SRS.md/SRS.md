# Software Requirements Specification (SRS)

## Project Name

MyWallet

---

## 1. Project Overview

MyWallet is a personal finance management application designed to help users manage their income, expenses, budgets, savings, and financial goals.

Unlike traditional expense trackers, MyWallet provides intelligent budget planning by analyzing previous spending patterns and recommending monthly budget allocations for different expense categories.

The application aims to help users build better financial habits through expense tracking, savings monitoring, budget warnings, and spending analytics.

## 2. Objectives

The objectives of MyWallet are:

- Help users monitor their daily expenses.
- Allow users to manage multiple income sources.
- Enable customizable expense categories.
- Suggest monthly budgets based on historical spending.
- Track savings and financial goals.
- Warn users when category budgets are nearly exhausted.
- Display meaningful spending analytics.
- Encourage smarter financial habits through data-driven recommendations.

## 3. Target Users

MyWallet is designed for:

- College Students
- Young Professionals
- Freelancers
- Individuals managing personal finances
- Anyone who wants better control over monthly spending

## 4. Functional Requirements

### User Management

- Create user profile
- Edit profile
- Set monthly income
- Set savings goal

### Income Management

- Add income
- Edit income
- Delete income
- Categorize income source

### Expense Management

- Add expense
- Edit expense
- Delete expense
- Search expenses
- Filter expenses
- View expense history

### Category Management

- View default categories
- Create custom category
- Edit category
- Delete category

### Budget Management

- Set monthly budget
- Set category-wise budget
- Receive budget warnings
- View remaining budget

### Savings

- Set savings goal
- Track savings progress

### Analytics

- Monthly spending summary
- Category-wise analysis
- Monthly comparison
- Spending trends
- Remaining budget

### Recommendation Engine

- Analyze previous spending
- Recommend category budgets
- Estimate monthly spending

## 5. Non-Functional Requirements

- Simple and intuitive interface
- Responsive design
- Fast loading screens
- Offline support
- Secure local data storage
- Easy navigation
- Modular code structure
- Scalable architecture
- Maintainable source code

## 6. System Modules

Module 1
User Profile

Module 2
Income Management

Module 3
Expense Management

Module 4
Budget Planner

Module 5
Savings Tracker

Module 6
Analytics Dashboard

Module 7
Recommendation Engine

Module 8
Settings

## 7. Database Overview

The application will use SQLite for local data storage.

The primary entities include:

- Users
- Income
- Expenses
- Categories
- Budgets
- Savings

Relationships between these entities will allow efficient storage, retrieval, and analysis of financial data.

## 8. Assumptions & Constraints

Assumptions:

- Users will regularly record their expenses.
- Users provide accurate income information.
- The application initially supports a single user.

Constraints:

- Internet connection is not required.
- Data is stored locally using SQLite.
- Investment tracking will not be included in Version 1.

## 9. Future Scope

- AI-powered financial assistant
- Automatic expense categorization
- Bank account integration
- Cloud synchronization
- Investment portfolio tracking
- Bill reminders
- Expense receipt scanning
- Export reports to PDF and Excel
- Multi-device synchronization
- Dark mode customization