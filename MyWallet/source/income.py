from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from database.models import Income
from app import db
from datetime import datetime

income = Blueprint('income', __name__)


@income.route('/income')
@login_required
def index():
    incomes = Income.query.filter_by(user_id=current_user.id).order_by(Income.date.desc()).all()
    return render_template('income/index.html', incomes=incomes)


@income.route('/income/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        new_income = Income(
            user_id=current_user.id,
            source=request.form.get('source'),
            amount=float(request.form.get('amount')),
            date=datetime.strptime(request.form.get('date'), '%Y-%m-%d').date(),
            note=request.form.get('note')
        )
        db.session.add(new_income)
        db.session.commit()
        flash('Income added!', 'success')
        return redirect(url_for('income.index'))
    return render_template('income/form.html', income=None)


@income.route('/income/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    inc = Income.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    if request.method == 'POST':
        inc.source = request.form.get('source')
        inc.amount = float(request.form.get('amount'))
        inc.date = datetime.strptime(request.form.get('date'), '%Y-%m-%d').date()
        inc.note = request.form.get('note')
        db.session.commit()
        flash('Income updated!', 'success')
        return redirect(url_for('income.index'))
    return render_template('income/form.html', income=inc)


@income.route('/income/delete/<int:id>', methods=['POST'])
@login_required
def delete(id):
    inc = Income.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    db.session.delete(inc)
    db.session.commit()
    flash('Income deleted.', 'info')
    return redirect(url_for('income.index'))
