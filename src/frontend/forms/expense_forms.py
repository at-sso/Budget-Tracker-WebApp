from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, SubmitField
from wtforms.validators import DataRequired


class BasicForm(FlaskForm):
    nombre = StringField("nombre", validators=[DataRequired()])
    monto = FloatField("monto", validators=[DataRequired()])
    submit = SubmitField("Add Expense")
