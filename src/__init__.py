from flask import (
    Flask,
    Response as FlaskResponse,
    redirect,
    render_template,
    request,
    jsonify,
    url_for,
)
from typing import (
    Any,
    List,
    Tuple,
)
from pymongo.cursor import Cursor

from src.backend.logger import *
from src.backend.database import *
from src.frontend.forms.delete_form import DeleteForm
from src.frontend.forms.edit_forms import EditForm
from src.frontend.forms.expense_forms import BasicForm

from flask_wtf import FlaskForm

CursorType = Cursor[Any]
JSONResponseType = Tuple[FlaskResponse, int]
ResponseType = Tuple[str, int]

app = Flask(__name__, template_folder="template", static_folder="frontend")

app.config['SECRET_KEY'] = "SECRET_KEY"


@app.route("/", methods=["GET", "POST"])
def index() -> str:
    "index() Renders the index.html template and returns it as a string."
    form = BasicForm()
    deleteForm= DeleteForm()
    editForm= EditForm()

    if form.validate_on_submit():
        nombre = form.nombre.data
        monto = form.monto.data
        registrar_gastos(nombre,monto) # type: ignore 
        return redirect(url_for('index'))
    if deleteForm.validate_on_submit():
    if editForm.validate_on_submit():
        modificar_gasto(editForm.editExpenseId.data, editForm.editNombre.data, editForm.editMonto.data) # type: ignore[warning]
        return ""
        eliminar_gasto(deleteForm.id_expense.data) # type: ignore
        return redirect(url_for('index'))
    return render_template("index.html", gastos = mostrar_gastos(), form=form, deleteForm=deleteForm, editForm=editForm)

@app.route("/expenses/<expense_id>", methods=["PUT"])
def update_expense(expense_id: str) -> ResponseType:  # Actualizar datos
    """Update an existing expense."""
    data: Any | None = request.json
    nombre = data.get("nombre")  # type: ignore[union-attr]
    monto = data.get("monto")  # type: ignore[union-attr]
    if nombre is None or monto is None:
        return "Missing data", 400
    modificar_gasto(expense_id, nombre, monto)
    return "Expense updated successfully", 200


