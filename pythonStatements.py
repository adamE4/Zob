# Import necessary modules and create Flask app
from app import app
from app.models import Temp
from app import db
# Create an application context
with app.app_context():
    # Inside this block, you have access to the app context, and you can work with the database session
    ob = Temp(name='adamelmo')
    db.session.add(ob)
    ob2 = Temp(name='Kyan')
    db.session.add(ob2)
    ob3 = Temp(name='Peter')
    db.session.add(ob3)
    
 
    # Commit the changes to the database
    db.session.commit()
    
