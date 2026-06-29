from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mywallet-secret-key-change-in-production'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myWallet.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from source.auth import auth
    from source.dashboard import dashboard
    from source.income import income
    from source.expense import expense
    from source.category import category
    from source.budget import budget
    from source.savings import savings
    from source.analytics import analytics

    app.register_blueprint(auth)
    app.register_blueprint(dashboard)
    app.register_blueprint(income)
    app.register_blueprint(expense)
    app.register_blueprint(category)
    app.register_blueprint(budget)
    app.register_blueprint(savings)
    app.register_blueprint(analytics)

    with app.app_context():
        db.create_all()
        from source.seed import seed_default_categories
        seed_default_categories()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
