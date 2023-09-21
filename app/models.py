from app import db
    

class recipes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    description = db.Column(db.String(250))
    ingredients = db.Column(db.String(100))
    instructions = db.Column(db.String(100))
    
     
