from flask import Blueprint, render_template
from flask_login import login_required, current_user
from database.models import Expense, Income, Budget, Saving, Category
from app import db
from datetime import datetime
from sqlalchemy import func

dashboard = Blueprint('dashboard', __name__)


@dashboard.route('/dashboard')
@login_required
def index():
    now = datetime.utcnow()
    month, year = now.month, now.year

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

    balance = total_income - total_expenses

    # Recent 5 expenses
    recent_expenses = Expense.query.filter_by(user_id=current_user.id)\
        .order_by(Expense.date.desc()).limit(5).all()

    # Budget warnings: categories where spent >= 80% of budget
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

    # Savings progress
    savings = Saving.query.filter_by(user_id=current_user.id).all()

    return render_template('dashboard/index.html',
        total_income=total_income,
        total_expenses=total_expenses,
        balance=balance,
        recent_expenses=recent_expenses,
        warnings=warnings,
        savings=savings,
        month_name=now.strftime('%B %Y')
    )
