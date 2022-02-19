from django.shortcuts import render
from app import app
from flask import render_template,redirect,url_for,flash,get_flashed_messages
from app.models import Item, User
from app.forms import RegisterForm
from app import db
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items=Item.query.all()
    return render_template('market.html',item_name=items)
@app.route('/register',methods=['GET','POST'])
def register_page():
    form=RegisterForm()
    if form.validate_on_submit():
        user_to_create=User(username=form.username.data,email_address=form.email.data,password_hash=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors !={}:
        for err_msg in form.errors.values():
            flash("There was an error")
    return render_template('register.html',form=form)
