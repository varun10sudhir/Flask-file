from flask_wtf import FlaskForm 
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length,EqualTo,Email,DataRequired

class RegisterForm(FlaskForm):
    username=StringField(label='Enter your username',validators=[Length(min=2,max=30),DataRequired()])
    email=StringField(label='Enter your email address',validators=[Email(),DataRequired()])
    password1=PasswordField(label='Enter your password',validators=[Length(min=6),DataRequired()])
    password2=PasswordField(label='Pls confirm your password',validators=[EqualTo('password1'),DataRequired()] )
    submit=SubmitField(label='Create account!')
