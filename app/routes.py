from flask import render_template, flash, redirect, url_for, request
from app import app,db
from app.models import recipes, User
from app.forms import postrecipes
from app.forms import LoginForm, RegisterForm
from flask_bcrypt import Bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, LoginManager, login_required, logout_user, current_user

bcrypt = Bcrypt()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"



@app.before_request
def initDB(*args, **kwargs):
    if app.got_first_request:
        db.create_all()

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html',recipe=None)



@app.route('/create_recipe', methods=['GET', 'POST'])
def create_recipe():
    cform = postrecipes()
    if cform.validate_on_submit():
        new_recipe = recipes(
            user_id = current_user.id,
            title=cform.title.data,
            description=cform.description.data,
            ingredients=cform.ingredients.data,
            instructions=cform.instructions.data  
        )
            
        db.session.add(new_recipe)
        db.session.commit()
        

        flash('Recipe created successfully', 'success')
        return redirect('dashboard')
    
    return render_template('recipes.html', form=cform)

@app.route('/recipe_feed')
def recipe_feed():
    user_recipe = recipes.query.filter_by(user_id=current_user.id).all()
    return render_template('feed.html', user_recipes=user_recipe)

@app.route('/view_recipe/<int:recipe_id>', methods=['GET'])
def view_recipe(recipe_id):
    recipe = recipes.query.get_or_404(recipe_id)
    return render_template('view_recipe.html', recipe=recipe)

@app.route('/share/<int:recipe_id>', methods=['GET'])
def share(recipe_id):
    recipe = recipes.query.get_or_404(recipe_id)
    shareable_link = url_for('view_recipe', recipe_id=recipe.id, _external=True)
    return render_template('share.html', shareable_link=shareable_link, recipe=recipe)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect('dashboard')
    return render_template('login.html', form=form)

@app.route('/dashboard',methods=['GET','POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html',form=form)

