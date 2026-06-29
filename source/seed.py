from database.models import Category
from app import db

DEFAULT_CATEGORIES = [
    {'name': 'Food & Dining', 'icon': '🍔'},
    {'name': 'Transport', 'icon': '🚌'},
    {'name': 'Housing', 'icon': '🏠'},
    {'name': 'Health', 'icon': '💊'},
    {'name': 'Education', 'icon': '📚'},
    {'name': 'Entertainment', 'icon': '🎬'},
    {'name': 'Shopping', 'icon': '🛍️'},
    {'name': 'Utilities', 'icon': '💡'},
    {'name': 'Personal Care', 'icon': '🪥'},
    {'name': 'Others', 'icon': '📦'},
]

def seed_default_categories():
    if Category.query.filter_by(is_default=True).first() is None:
        for cat in DEFAULT_CATEGORIES:
            db.session.add(Category(name=cat['name'], icon=cat['icon'], is_default=True))
        db.session.commit()