from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, form, SelectField
from wtforms.validators import  ValidationError, Length, InputRequired
from app.models import User

class postrecipes(FlaskForm):
    title = StringField('Title', validators=[Length(max=30)])
    description = StringField('Description', validators=[Length(max=250)])
    ingredients = StringField('Ingredients', validators=[Length(max=100)])
    instructions = StringField('Instructions', validators=[Length(max=100)])
    
    submit = SubmitField('Submit')
    
class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(),Length(
       min=4,max=20)], render_kw={"placeholder": "Username"})
    
    password = PasswordField(validators=[InputRequired(),Length(
        min=4, max=20)], render_kw={"placeholder": "Password"})
    
    submit = SubmitField("Register")
    
    def validate_username(self, username):
      user = User.query.filter_by(username=username.data).first()
      if user:
        raise ValidationError("That username already exists. Please choose a different one.")
         
class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(),Length(
       min=4,max=20)], render_kw={"placeholder": "Username"})
    
    password = PasswordField(validators=[InputRequired(),Length(
        min=4, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Login")
        
class RecipesearchForm(FlaskForm):
    select = SubmitField('Search:')
    search = StringField('Search for recipes')