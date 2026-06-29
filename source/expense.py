from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from database.models import Expense, Category
from database.models import db
from datetime import datetime

expense = Blueprint('expense', __name__)


def get_categories():
    return Category.query.filter(
        (Category.is_default == True) | (Category.user_id == current_user.id)
    ).all()


@expense.route('/expenses')
@login_required
def index():
    q = request.args.get('q', '')
    category_id = request.args.get('category_id', '')
    month = request.args.get('month', '')

    query = Expense.query.filter_by(user_id=current_user.id)

    if q:
        query = query.filter(Expense.title.ilike(f'%{q}%'))
    if category_id:
        query = query.filter_by(category_id=int(category_id))
    if month:
        query = query.filter(
            db.func.strftime('%Y-%m', Expense.date) == month
        )

    expenses = query.order_by(Expense.date.desc()).all()
    categories = get_categories()
    return render_template('expense/index.html', expenses=expenses, categories=categories, q=q)


@expense.route('/expenses/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        new_expense = Expense(
            user_id=current_user.id,
            category_id=int(request.form.get('category_id')),
            title=request.form.get('title'),
            amount=float(request.form.get('amount')),
            date=datetime.strptime(request.form.get('date'), '%Y-%m-%d').date(),
            note=request.form.get('note')
        )
        db.session.add(new_expense)
        db.session.commit()
        flash('Expense added!', 'success')
        return redirect(url_for('expense.index'))
    return render_template('expense/form.html', expense=None, categories=get_categories())


@expense.route('/expenses/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    exp = Expense.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    if request.method == 'POST':
        exp.category_id = int(request.form.get('category_id'))
        exp.title = request.form.get('title')
        exp.amount = float(request.form.get('amount'))
        exp.date = datetime.strptime(request.form.get('date'), '%Y-%m-%d').date()
        exp.note = request.form.get('note')
        db.session.commit()
        flash('Expense updated!', 'success')
        return redirect(url_for('expense.index'))
    return render_template('expense/form.html', expense=exp, categories=get_categories())


@expense.route('/expenses/delete/<int:id>', methods=['POST'])
@login_required
def delete(id):
    exp = Expense.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    db.session.delete(exp)
    db.session.commit()
    flash('Expense deleted.', 'info')
    return redirect(url_for('expense.index'))
