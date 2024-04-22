from flask_wtf import FlaskForm  # type: ignore[import-untyped]
from wtforms import FloatField, StringField, SubmitField  # type: ignore[import-untyped]
from wtforms.validators import DataRequired  # type: ignore[import-untyped]


class BasicForm(FlaskForm):
    """
    The `BasicForm` class defines a basic form for adding an expense entry.

    @param nombre The `nombre` parameter in the `BasicForm` class is a string representing
    the name of the expense entry to be added. It is validated to be non-empty.
    @param monto The `monto` parameter in the `BasicForm` class is a float representing
    the amount of the expense entry to be added. It is validated to be non-empty.

    @return None
    """

    nombre = StringField("nombre", validators=[DataRequired()])
    monto = FloatField("monto", validators=[DataRequired()])
    submit = SubmitField("Add Expense")
