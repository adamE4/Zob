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
    return render_template('index.html',recipe=None)



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

@app.route('/view_recipe/<int:recipe_id>', methods=['GET'])
def view_recipe(recipe_id):
    recipe = recipes.query.get_or_404(recipe_id)
    return render_template('view_recipe.html', recipe=recipe)

@app.route('/share/<int:recipe_id>', methods=['GET'])
def share(recipe_id):
    recipe = recipes.query.get_or_404(recipe_id)
    shareable_link = url_for('view_recipe', recipe_id=recipe.id, _external=True)
    return render_template('share.html', shareable_link=shareable_link, recipe=recipe)


