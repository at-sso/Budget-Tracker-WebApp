from flask import (
    Flask,
    Response as FlaskResponse,
    redirect,
    render_template,
    request,
    url_for,
)
from typing import (
    Any,
    Tuple,
)
from pymongo.cursor import Cursor

from src.backend.logger import *
from src.backend.database import *
from src.frontend.forms.delete_form import DeleteForm
from src.frontend.forms.edit_forms import EditForm
from src.frontend.forms.expense_forms import BasicForm

from flask_wtf import FlaskForm  # type: ignore[import-untyped]

CursorType = Cursor[Any]
JSONResponseType = Tuple[FlaskResponse, int]
ResponseType = Tuple[str, int]

app = Flask(__name__, template_folder="template", static_folder="frontend")

app.config["SECRET_KEY"] = "SECRET_KEY"

with app.app_context():
    MISSING_DATA: ResponseType = "Missing data", 400
    UPDATED_SUCCESSFULLY: ResponseType = "Expense updated successfully", 200


@app.route("/", methods=["GET", "POST"])
def index() -> Any:
    """
    index() Renders the index.html template and returns it as a string.

    @return The function index is returning the rendered HTML template as a string. If any errors occur during
    this process, they are handled internally, and appropriate redirections are performed.
    """
    basic_form = BasicForm()
    delete_form = DeleteForm()
    edit_form = EditForm()

    if basic_form.validate_on_submit():
        nombre: str | Any = basic_form.nombre.data
        monto: float | Any = basic_form.monto.data
        registrar_gastos(nombre, monto)  # type: ignore[warning]
        return redirect(url_for("index"))
    if edit_form.validate_on_submit():
        modificar_gasto(edit_form.editExpenseId.data, edit_form.editNombre.data, edit_form.editMonto.data)  # type: ignore[warning]
        return redirect(url_for("index"))

    if delete_form.validate_on_submit():
        eliminar_gasto(delete_form.id_expense.data)  # type: ignore[warning]
        return redirect(url_for("index"))
    return render_template(
        "index.html",
        gastos=mostrar_gastos(),
        form=basic_form,
        deleteForm=delete_form,
        editForm=edit_form,
    )


@app.route("/expenses/<expense_id>", methods=["PUT"])
def update_expense(expense_id: str) -> ResponseType:  # Actualizar datos
    """
    Update an existing expense.

    @param expense_id The `expense_id` parameter in the `update_expense` function is a string that represents
    the unique identifier of the expense to be updated.

    @return The function `update_expense` returns a tuple consisting of a string `"Missing data"` and an
    integer `400` representing a response indicating that the request is missing data, if either the `nombre`
    or `monto` attributes are missing from the JSON data in the request. If the data is successfully updated,
    the function returns a tuple with the string `"Expense updated successfully"` and the integer `200`.
    """
    data: Any = request.json
    nombre: Any = data.get("nombre")  # type: ignore[union-attr]
    monto: Any = data.get("monto")  # type: ignore[union-attr]
    if nombre is None or monto is None:
        return MISSING_DATA
    modificar_gasto(expense_id, nombre, monto)
    return UPDATED_SUCCESSFULLY
