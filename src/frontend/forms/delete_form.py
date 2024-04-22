from flask_wtf import FlaskForm  # type: ignore[import-untyped]
from wtforms import FloatField, StringField, SubmitField  # type: ignore[import-untyped]
from wtforms.validators import DataRequired  # type: ignore[import-untyped]


class DeleteForm(FlaskForm):
    """
    The `DeleteForm` class defines a form for deleting an expense entry.

    @param id_expense The `id_expense` parameter in the `DeleteForm` class is a string representing
    the ID of the expense entry to be deleted.

    @return None
    """

    id_expense = StringField("id_expense")
    submit = SubmitField("Eliminar")
