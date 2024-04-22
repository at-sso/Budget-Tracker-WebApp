from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, SubmitField  # type: ignore[warning]
from wtforms.validators import DataRequired  # type: ignore[warning]


class DeleteForm(FlaskForm):
    id_expense = StringField("id_expense")
    submit = SubmitField("Eliminar")
