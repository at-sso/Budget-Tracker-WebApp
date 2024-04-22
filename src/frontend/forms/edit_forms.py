from flask_wtf import FlaskForm  # type: ignore[import-untyped]
from wtforms import FloatField, StringField, SubmitField  # type: ignore[import-untyped]
from wtforms.validators import DataRequired  # type: ignore[import-untyped]


class EditForm(FlaskForm):
    """
    The `EditForm` class defines a form for editing an expense entry.

    @param editNombre The `editNombre` parameter in the `EditForm` class is a string representing
    the name of the expense entry to be edited. It is validated to be non-empty.
    @param editMonto The `editMonto` parameter in the `EditForm` class is a float representing
    the amount of the expense entry to be edited. It is validated to be non-empty.
    @param editExpenseId The `editExpenseId` parameter in the `EditForm` class is a string representing
    the ID of the expense entry to be edited.

    @return None
    """

    editNombre = StringField("", validators=[DataRequired()])
    editMonto = FloatField("10", validators=[DataRequired()])
    editExpenseId = StringField("")
    submit = SubmitField("Guardar")
