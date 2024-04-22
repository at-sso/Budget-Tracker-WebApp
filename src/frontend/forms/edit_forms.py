from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, SubmitField
from wtforms.validators import DataRequired


class EditForm(FlaskForm):
    editNombre = StringField("", validators=[DataRequired()])
    editMonto = FloatField("10", validators=[DataRequired()])
    editExpenseId = StringField("")
    submit = SubmitField("Guardar")
