from flask import render_template, flash, redirect, url_for, request
from app import app,db
from app.models import Temp

@app.before_request
def initDB(*args, **kwargs):
    if app.got_first_request:
        db.create_all()

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    users = Temp.query.all()
    return render_template('index.html',temp=users)


@app.route('/temp',methods=['GET'])
def T():
     users = Temp.query.all()
     return render_template('temp.html',temp=users)
