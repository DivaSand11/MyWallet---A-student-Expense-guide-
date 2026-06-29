from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from database.models import Budget, Expense, Category
from database.models import db
from datetime import datetime
from sqlalchemy import func

budget = Blueprint('budget', __name__)


@budget.route('/budget')
@login_required
def index():
    now = datetime.utcnow()
    month = int(request.args.get('month', now.month))
    year = int(request.args.get('year', now.year))

    budgets = Budget.query.filter_by(user_id=current_user.id, month=month, year=year).all()
    budget_data = []
    for b in budgets:
        spent = db.session.query(func.sum(Expense.amount)).filter(
            Expense.user_id == current_user.id,
            Expense.category_id == b.category_id,
            func.strftime('%m', Expense.date) == f'{month:02d}',
            func.strftime('%Y', Expense.date) == str(year)
        ).scalar() or 0
        percent = round((spent / b.amount) * 100) if b.amount > 0 else 0
        budget_data.append({
            'id': b.id,
            'category': b.category.name,
            'icon': b.category.icon,
            'budget': b.amount,
            'spent': spent,
            'remaining': b.amount - spent,
            'percent': min(percent, 100),
            'warning': percent >= 80
        })

    categories = Category.query.filter(
        (Category.is_default == True) | (Category.user_id == current_user.id)
    ).all()

    return render_template('budget/index.html', budget_data=budget_data,
                           categories=categories, month=month, year=year)


@budget.route('/budget/set', methods=['POST'])
@login_required
def set_budget():
    category_id = int(request.form.get('category_id'))
    amount = float(request.form.get('amount'))
    month = int(request.form.get('month'))
    year = int(request.form.get('year'))

    existing = Budget.query.filter_by(
        user_id=current_user.id, category_id=category_id, month=month, year=year
    ).first()

    if existing:
        existing.amount = amount
    else:
        db.session.add(Budget(user_id=current_user.id, category_id=category_id,
                              amount=amount, month=month, year=year))
    db.session.commit()
    flash('Budget saved!', 'success')
    return redirect(url_for('budget.index', month=month, year=year))


@budget.route('/budget/delete/<int:id>', methods=['POST'])
@login_required
def delete(id):
    b = Budget.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    db.session.delete(b)
    db.session.commit()
    flash('Budget removed.', 'info')
    return redirect(url_for('budget.index'))
