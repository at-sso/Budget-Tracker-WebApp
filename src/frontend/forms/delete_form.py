from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, SubmitField
from wtforms.validators import DataRequired

class DeleteForm(FlaskForm):
    id_expense = StringField("id_expense")
    submit = SubmitField("Eliminar")
    