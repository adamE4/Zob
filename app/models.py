from app import db

class Temp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))  
