from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
import time

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)

@app.route('/seed')
def seed_data():
    Item.query.delete()
    db.session.commit()

    items = [
        {"title": "Test 1", "description": "Demo"},
        {"title": "Test 2", "description": "Demo2"}
    ]

    for i in items:
        db.session.add(Item(title=i['title'], description=i['description']))

    db.session.commit()

    return "Seeded!"

@app.route('/items')
def get_items():
    items = Item.query.all()
    return [
        {
            "id": i.id,
            "title": i.title,
            "description": i.description
        }
        for i in items
    ]

@app.route('/')
def home():
    return "Backend OK"

if __name__ == '__main__':
    with app.app_context():
        for i in range(10):
            try:
                db.create_all()
                print("DB connected!")
                break
            except:
                print("Waiting for DB...")
                time.sleep(2)

    app.run(host='0.0.0.0', port=5000)