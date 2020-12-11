from flask_wtf import FlaskForm
from flask_wtf import Form
from wtforms import StringField, TextField, SubmitField, IntegerField,TextAreaField,RadioField,SelectField, DecimalField
from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.validators import ValidationError

class PredictForm(FlaskForm):
	Wind_Speed = DecimalField('Wind Speed (m/s)')
	Theoretical_Power_Curve = DecimalField('Theoretical_Power_Curve (KWh)')
	Wind_Direction = DecimalField('Wind Direction (°)')
	submit = SubmitField('Predict')
	abc = "" 