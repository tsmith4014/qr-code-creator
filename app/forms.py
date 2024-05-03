# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class InputForm(FlaskForm):
    info1 = StringField('Enter Your Username')
    info1_additional1 = StringField('Enter Your Password')
    submit1 = SubmitField('Generate QR Code for Form 1')
    info2 = StringField('Enter Information for Form 2')
    submit2 = SubmitField('Generate QR Code for Form 2')
    info3 = StringField('Enter Information for Form 3')
    submit3 = SubmitField('Generate QR Code for Form 3')
    info4 = StringField('Enter Information for Form 4')
    submit4 = SubmitField('Generate QR Code for Form 4')
