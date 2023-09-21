from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import  ValidationError, Length

class postrecipes(FlaskForm):
    title = StringField('Title', validators=[Length(max=30)])
    description = StringField('Description', validators=[Length(max=250)])
    ingredients = StringField('Ingredients', validators=[Length(max=100)])
    instructions = StringField('Instructions', validators=[Length(max=100)])
    
    submit = SubmitField('Submit')
    

