from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__,template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///market.db'
app.config['SECRET_KEY']='1f1ea6a3175e85491b795413'
db=SQLAlchemy(app)

from app import routes