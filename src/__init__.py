from flask import (
    Flask,
    Response as FlaskResponse,
    render_template,
    request,
    jsonify,
)
from typing import (
    Any,
    List,
    Tuple,
)
from pymongo.cursor import Cursor

from src.backend.logger import *
from src.backend.database import *

CursorType = Cursor[Any]
JSONResponseType = Tuple[FlaskResponse, int]
ResponseType = Tuple[str, int]

app = Flask(__name__, template_folder="template", static_folder="frontend")


@app.route("/")
def index() -> str:
    "index() Renders the index.html template and returns it as a string."
    return render_template("index.html")


@app.route("/expenses", methods=["GET"])
def get_expenses() -> JSONResponseType:  # Obtener todos los datos
    """Get all expenses from the database."""
    expenses: List[JSONType] = mostrar_gastos()
    return jsonify(expenses), 200


@app.route("/expenses", methods=["POST"])
def add_expense() -> ResponseType:  # Añadir datos
    """Add a new expense."""
    data: Any | None = request.json
    nombre = data.get("nombre")  # type: ignore[union-attr]
    monto = data.get("monto")  # type: ignore[union-attr]
    if nombre is None or monto is None:
        return "Missing data", 400
    registrar_gastos(nombre, monto)
    return "Expense added successfully", 201


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


@app.route("/expenses/<expense_id>", methods=["DELETE"])
def delete_expense(expense_id: str) -> ResponseType:  # Eliminar datos
    """Delete an expense."""
    eliminar_gasto(expense_id)
    return "Expense deleted successfully", 200
