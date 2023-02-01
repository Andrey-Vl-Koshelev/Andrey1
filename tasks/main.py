from tasks.app import db
from tasks.app import app


with app.app_context():
    db.create_all()

