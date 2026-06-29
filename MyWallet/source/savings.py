from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from database.models import Saving
from app import db
from datetime import datetime

savings = Blueprint('savings', __name__)


@savings.route('/savings')
@login_required
def index():
    all_savings = Saving.query.filter_by(user_id=current_user.id).all()
    savings_data = []
    for s in all_savings:
        percent = round((s.saved_amount / s.goal_amount) * 100) if s.goal_amount > 0 else 0
        savings_data.append({
            'obj': s,
            'percent': min(percent, 100),
            'remaining': s.goal_amount - s.saved_amount
        })
    return render_template('savings/index.html', savings_data=savings_data)


@savings.route('/savings/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        deadline_str = request.form.get('deadline')
        deadline = datetime.strptime(deadline_str, '%Y-%m-%d').date() if deadline_str else None
        s = Saving(
            user_id=current_user.id,
            title=request.form.get('title'),
            goal_amount=float(request.form.get('goal_amount')),
            saved_amount=float(request.form.get('saved_amount', 0)),
            deadline=deadline
        )
        db.session.add(s)
        db.session.commit()
        flash('Savings goal added!', 'success')
        return redirect(url_for('savings.index'))
    return render_template('savings/form.html', saving=None)


@savings.route('/savings/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    s = Saving.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    if request.method == 'POST':
        s.title = request.form.get('title')
        s.goal_amount = float(request.form.get('goal_amount'))
        s.saved_amount = float(request.form.get('saved_amount', 0))
        deadline_str = request.form.get('deadline')
        s.deadline = datetime.strptime(deadline_str, '%Y-%m-%d').date() if deadline_str else None
        db.session.commit()
        flash('Savings goal updated!', 'success')
        return redirect(url_for('savings.index'))
    return render_template('savings/form.html', saving=s)


@savings.route('/savings/delete/<int:id>', methods=['POST'])
@login_required
def delete(id):
    s = Saving.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    db.session.delete(s)
    db.session.commit()
    flash('Savings goal deleted.', 'info')
    return redirect(url_for('savings.index'))
