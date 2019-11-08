from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField

class ReceiveForm(FlaskForm):
	name = StringField('Name')
	pname= SelectField('Title', choices=[('Feeding India', 'Feeding India'),
                                 ('Kids For Tigers', 'Kids For Tigers'),
                                 ('Fund Raiser For Kids', 'Fund Raiser For Kids'),
                                 ('Save Water', 'Save Water')])
	submit = SubmitField('Search')