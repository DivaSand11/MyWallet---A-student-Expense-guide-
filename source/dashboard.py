from flask import Blueprint, render_template
from flask_login import login_required, current_user
from database.models import Expense, Income, Budget, Saving, Category
from database.models import db
from datetime import datetime, date
from sqlalchemy import func
import calendar

dashboard = Blueprint('dashboard', __name__)


@dashboard.route('/dashboard')
@login_required
def index():
    now = datetime.utcnow()
    today = date.today()
    month, year = now.month, now.year
    days_in_month = calendar.monthrange(year, month)[1]
    days_left = days_in_month - today.day + 1

    # Total income this month
    total_income = db.session.query(func.sum(Income.amount)).filter(
        Income.user_id == current_user.id,
        func.strftime('%m', Income.date) == f'{month:02d}',
        func.strftime('%Y', Income.date) == str(year)
    ).scalar() or 0

    # Total expenses this month
    total_expenses = db.session.query(func.sum(Expense.amount)).filter(
        Expense.user_id == current_user.id,
        func.strftime('%m', Expense.date) == f'{month:02d}',
        func.strftime('%Y', Expense.date) == str(year)
    ).scalar() or 0

    # Today's expenses
    today_expenses = db.session.query(func.sum(Expense.amount)).filter(
        Expense.user_id == current_user.id,
        Expense.date == today
    ).scalar() or 0

    balance = total_income - total_expenses

    # Daily budget = remaining balance / days left in month
    daily_limit = round(balance / days_left, 2) if days_left > 0 else 0
    remaining_today = round(daily_limit - today_expenses, 2)

    # Recent 5 expenses
    recent_expenses = Expense.query.filter_by(user_id=current_user.id)\
        .order_by(Expense.date.desc()).limit(5).all()

    # Budget warnings
    budgets = Budget.query.filter_by(user_id=current_user.id, month=month, year=year).all()
    warnings = []
    for b in budgets:
        spent = db.session.query(func.sum(Expense.amount)).filter(
            Expense.user_id == current_user.id,
            Expense.category_id == b.category_id,
            func.strftime('%m', Expense.date) == f'{month:02d}',
            func.strftime('%Y', Expense.date) == str(year)
        ).scalar() or 0
        if b.amount > 0 and spent / b.amount >= 0.8:
            warnings.append({
                'category': b.category.name,
                'icon': b.category.icon,
                'spent': spent,
                'budget': b.amount,
                'percent': round((spent / b.amount) * 100)
            })

    # Smart suggestions
    suggestions = []
    if remaining_today < 0:
        suggestions.append({'icon': '🚨', 'text': f"You've exceeded today's limit by ₹{abs(remaining_today):.0f}. Try to avoid any more spending today."})
    elif remaining_today < daily_limit * 0.3:
        suggestions.append({'icon': '⚠️', 'text': f"Only ₹{remaining_today:.0f} left for today. Spend carefully!"})
    else:
        suggestions.append({'icon': '✅', 'text': f"You're on track! ₹{remaining_today:.0f} left to spend today."})

    if total_expenses > total_income * 0.9:
        suggestions.append({'icon': '💡', 'text': "You've used over 90% of your income this month. Consider cutting discretionary spending."})

    if not budgets:
        suggestions.append({'icon': '📋', 'text': "You haven't set any budgets yet. Set category budgets to track spending better."})

    savings = Saving.query.filter_by(user_id=current_user.id).all()

    return render_template('dashboard/index.html',
        total_income=total_income,
        total_expenses=total_expenses,
        today_expenses=today_expenses,
        balance=balance,
        daily_limit=daily_limit,
        remaining_today=remaining_today,
        days_left=days_left,
        recent_expenses=recent_expenses,
        warnings=warnings,
        suggestions=suggestions,
        savings=savings,
        month_name=now.strftime('%B %Y'),
        today=today.strftime('%d %b %Y')
    )