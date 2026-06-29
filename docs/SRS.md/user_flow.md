# User Flow Document

# Project Name

**MyWallet**

---

# 1. Purpose

This document describes the complete journey of a user while interacting with the MyWallet application. It defines how users navigate through the application, what actions they perform, and how the system responds at every stage.

The objective is to ensure a simple, intuitive, and user-friendly experience.

---

# 2. First-Time User Flow

When the application is launched for the first time:

```
Splash Screen
        ↓
Welcome Screen
        ↓
Create Profile
        ↓
Enter Monthly Income
        ↓
Set Savings Goal
        ↓
Choose Default Categories
        ↓
Dashboard
```

### Step Description

### Splash Screen

Displays:

* MyWallet Logo
* App Name
* Tagline

```
Track Smart. Save Smarter.
```

Automatically navigates to the Welcome Screen.

---

### Welcome Screen

Purpose:

Introduce the application.

Buttons:

* Get Started

---

### Create Profile

User enters:

* Name
* Preferred Currency
* Monthly Income

Presses:

**Continue**

---

### Savings Goal

User sets:

* Monthly Savings Goal

Example:

```
₹3000
```

The application will use this value while recommending monthly budgets.

---

### Category Selection

Default Categories:

* Food
* Travel
* Education
* Shopping
* Entertainment
* Health
* Recharge
* Others

The user may:

* Keep default categories
* Add custom categories
* Remove unnecessary categories

---

### Dashboard

After completing setup, the user reaches the Home Dashboard.

---

# 3. Returning User Flow

Returning users directly open:

```
Splash Screen
        ↓
Dashboard
```

No onboarding is shown again.

---

# 4. Dashboard Flow

Dashboard displays:

* Monthly Income
* Remaining Budget
* Total Expenses
* Savings
* Investment Summary (Future Version)
* Budget Progress
* Recent Expenses
* Quick Actions

Quick Actions:

* Add Expense
* Add Income
* View Analytics

Navigation:

Bottom Navigation Bar

Home

Analytics

Goals

Profile

---

# 5. Add Expense Flow

```
Dashboard
      ↓
Add Expense
      ↓
Fill Expense Details
      ↓
Save
      ↓
Database Updated
      ↓
Dashboard Updated
```

Expense Details:

* Amount
* Category
* Description
* Date
* Payment Method
* Notes (Optional)

System Response:

* Expense stored
* Budget updated
* Remaining budget recalculated
* Analytics refreshed

---

# 6. Add Income Flow

```
Dashboard
      ↓
Add Income
      ↓
Enter Details
      ↓
Save
      ↓
Dashboard Updated
```

Income Details:

* Amount
* Source
* Date
* Notes

Examples:

* Pocket Money
* Internship
* Scholarship
* Freelancing
* Gifts

---

# 7. Budget Planner Flow

```
New Month Begins
        ↓
Analyze Previous Spending
        ↓
Generate Recommended Budget
        ↓
User Reviews Suggestions
        ↓
User Modifies (Optional)
        ↓
Budget Saved
```

Recommendation Example:

Food

₹3200

Travel

₹700

Education

₹1800

Entertainment

₹1000

Savings

₹2000

---

# 8. Budget Warning Flow

Whenever an expense is added:

```
Check Category Budget
        ↓
Remaining Budget?
        ↓
If Safe → Continue
If Low → Show Warning
If Exceeded → Alert User
```

Example:

```
Food Budget

₹3500

Spent

₹3300

Remaining

₹200

Warning:

You are about to exceed your Food budget.
```

---

# 9. Analytics Flow

```
Dashboard
      ↓
Analytics
```

Displays:

* Monthly Spending
* Category Distribution
* Weekly Spending
* Highest Expense Category
* Average Daily Spending
* Remaining Budget
* Savings Progress

Future:

AI Spending Insights

---

# 10. Savings Flow

```
Dashboard
      ↓
Savings
```

Displays:

* Savings Goal
* Current Savings
* Remaining Amount
* Goal Progress

Example:

Goal

₹50,000

Saved

₹18,000

36%

---

# 11. Category Management

```
Profile
      ↓
Categories
```

User can:

* Add Category
* Edit Category
* Delete Category

Changes immediately affect future expenses.

---

# 12. Profile Flow

```
Dashboard
      ↓
Profile
```

User can edit:

* Name
* Monthly Income
* Savings Goal
* Currency

Future:

* Theme
* Notifications
* Cloud Backup

---

# 13. Exit Flow

When the application closes:

* All data remains stored in SQLite.
* User settings are preserved.
* Dashboard opens directly during the next launch.

---

# 14. Future User Flow

Version 2

* Login / Signup
* Cloud Sync
* Multiple Devices
* Investment Tracking
* AI Financial Assistant
* Bank Integration
* Expense Receipt Scanner
* Bill Reminders

---

# User Journey Summary

```
Open App
        ↓
Profile Setup (First Time Only)
        ↓
Dashboard
        ↓
Add Income / Add Expense
        ↓
Budget Updated
        ↓
Analytics Updated
        ↓
Savings Updated
        ↓
Monthly Budget Recommendation
        ↓
Continue Managing Finances
```
