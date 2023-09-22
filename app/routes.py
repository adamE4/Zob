from flask import render_template, flash, redirect, url_for, request
from app import app,db
from app.models import recipes
from app.forms import postrecipes

@app.before_request
def initDB(*args, **kwargs):
    if app.got_first_request:
        db.create_all()

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')



@app.route('/create_recipe', methods=['GET', 'POST'])
def create_recipe():
    cform = postrecipes()
    
    if cform.validate_on_submit():

        new_recipe = recipes(
            title=cform.title.data,
            description=cform.description.data,
            ingredients=cform.ingredients.data,
            instructions=cform.instructions.data
        )
        

        db.session.add(new_recipe)
        db.session.commit()
        

        flash('Recipe created successfully', 'success')
        return redirect('/index')
    
    return render_template('recipes.html', form=cform)

@app.route('/recipe_feed')
def recipe_feed():
    recipe_list = recipes.query.all()  
    return render_template('feed.html', recipes=recipe_list)

