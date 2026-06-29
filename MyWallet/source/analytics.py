from flask import Blueprint, render_template, jsonify
from flask_login import login_required, current_user
from database.models import Expense, Income, Category
from app import db
from datetime import datetime
from sqlalchemy import func
from collections import defaultdict

analytics = Blueprint('analytics', __name__)


def get_monthly_expenses(user_id, month, year):
    return db.session.query(func.sum(Expense.amount)).filter(
        Expense.user_id == user_id,
        func.strftime('%m', Expense.date) == f'{month:02d}',
        func.strftime('%Y', Expense.date) == str(year)
    ).scalar() or 0


@analytics.route('/analytics')
@login_required
def index():
    now = datetime.utcnow()

    # Category-wise spending this month
    category_data = db.session.query(
        Category.name, Category.icon, func.sum(Expense.amount)
    ).join(Expense, Expense.category_id == Category.id)\
     .filter(
        Expense.user_id == current_user.id,
        func.strftime('%m', Expense.date) == f'{now.month:02d}',
        func.strftime('%Y', Expense.date) == str(now.year)
    ).group_by(Category.id).all()

    # Last 6 months comparison
    monthly_totals = []
    for i in range(5, -1, -1):
        m = (now.month - i - 1) % 12 + 1
        y = now.year if now.month - i > 0 else now.year - 1
        total = get_monthly_expenses(current_user.id, m, y)
        monthly_totals.append({
            'label': datetime(y, m, 1).strftime('%b %Y'),
            'total': total
        })

    # Recommendation engine: avg spending per category last 3 months
    recommendations = []
    categories = Category.query.filter(
        (Category.is_default == True) | (Category.user_id == current_user.id)
    ).all()

    for cat in categories:
        monthly_spends = []
        for i in range(1, 4):
            m = (now.month - i - 1) % 12 + 1
            y = now.year if now.month - i > 0 else now.year - 1
            spent = db.session.query(func.sum(Expense.amount)).filter(
                Expense.user_id == current_user.id,
                Expense.category_id == cat.id,
                func.strftime('%m', Expense.date) == f'{m:02d}',
                func.strftime('%Y', Expense.date) == str(y)
            ).scalar() or 0
            monthly_spends.append(spent)

        if any(s > 0 for s in monthly_spends):
            avg = sum(monthly_spends) / len([s for s in monthly_spends if s > 0])
            recommendations.append({
                'category': cat.name,
                'icon': cat.icon,
                'avg_spending': round(avg, 2),
                'suggested_budget': round(avg * 1.1, 2)
            })

    return render_template('analytics/index.html',
        category_data=category_data,
        monthly_totals=monthly_totals,
        recommendations=recommendations,
        month_name=now.strftime('%B %Y')
    )


@analytics.route('/analytics/data')
@login_required
def data():
    now = datetime.utcnow()

    cat_labels = []
    cat_values = []
    rows = db.session.query(
        Category.name, func.sum(Expense.amount)
    ).join(Expense, Expense.category_id == Category.id)\
     .filter(
        Expense.user_id == current_user.id,
        func.strftime('%m', Expense.date) == f'{now.month:02d}',
        func.strftime('%Y', Expense.date) == str(now.year)
    ).group_by(Category.id).all()

    for name, total in rows:
        cat_labels.append(name)
        cat_values.append(round(total, 2))

    monthly_labels = []
    monthly_values = []
    for i in range(5, -1, -1):
        m = (now.month - i - 1) % 12 + 1
        y = now.year if now.month - i > 0 else now.year - 1
        monthly_labels.append(datetime(y, m, 1).strftime('%b'))
        monthly_values.append(get_monthly_expenses(current_user.id, m, y))

    return jsonify({
        'category': {'labels': cat_labels, 'values': cat_values},
        'monthly': {'labels': monthly_labels, 'values': monthly_values}
    })
