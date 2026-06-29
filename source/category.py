from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from database.models import Category
from database.models import db

category = Blueprint('category', __name__)


@category.route('/categories')
@login_required
def index():
    defaults = Category.query.filter_by(is_default=True).all()
    custom = Category.query.filter_by(user_id=current_user.id, is_default=False).all()
    return render_template('category/index.html', defaults=defaults, custom=custom)


@category.route('/categories/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        cat = Category(
            name=request.form.get('name'),
            icon=request.form.get('icon', '📦'),
            user_id=current_user.id,
            is_default=False
        )
        db.session.add(cat)
        db.session.commit()
        flash('Category created!', 'success')
        return redirect(url_for('category.index'))
    return render_template('category/form.html', category=None)


@category.route('/categories/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    cat = Category.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    if request.method == 'POST':
        cat.name = request.form.get('name')
        cat.icon = request.form.get('icon', '📦')
        db.session.commit()
        flash('Category updated!', 'success')
        return redirect(url_for('category.index'))
    return render_template('category/form.html', category=cat)


@category.route('/categories/delete/<int:id>', methods=['POST'])
@login_required
def delete(id):
    cat = Category.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    db.session.delete(cat)
    db.session.commit()
    flash('Category deleted.', 'info')
    return redirect(url_for('category.index'))
