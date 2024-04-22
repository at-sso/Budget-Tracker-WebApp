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

from flask_wtf import FlaskForm  # type: ignore[warning]

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
    "index() Renders the index.html template and returns it as a string."
    form = BasicForm()
    deleteForm = DeleteForm()
    editForm = EditForm()
    if form.validate_on_submit():
        nombre: str | Any = form.nombre.data
        monto: float | Any = form.monto.data
        registrar_gastos(nombre, monto)  # type: ignore
        return redirect(url_for("index"))
    if editForm.validate_on_submit():
        modificar_gasto(editForm.editExpenseId.data, editForm.editNombre.data, editForm.editMonto.data)  # type: ignore[warning]
        return redirect(url_for("index"))

    if deleteForm.validate_on_submit():
        eliminar_gasto(deleteForm.id_expense.data)  # type: ignore
        return redirect(url_for("index"))
    return render_template(
        "index.html",
        gastos=mostrar_gastos(),
        form=form,
        deleteForm=deleteForm,
        editForm=editForm,
    )


@app.route("/expenses/<expense_id>", methods=["PUT"])
def update_expense(expense_id: str) -> ResponseType:  # Actualizar datos
    """Update an existing expense."""
    data: Any = request.json
    nombre: Any = data.get("nombre")  # type: ignore[union-attr]
    monto: Any = data.get("monto")  # type: ignore[union-attr]
    if nombre is None or monto is None:
        return MISSING_DATA
    modificar_gasto(expense_id, nombre, monto)
    return UPDATED_SUCCESSFULLY
