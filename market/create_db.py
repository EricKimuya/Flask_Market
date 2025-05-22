from market import app, db

with app.app_context():
    db.create_all()    # filepath: /home/eric/Projects/FlaskMarket/create_db.py
    from market import app, db
    
    with app.app_context():
        db.create_all()