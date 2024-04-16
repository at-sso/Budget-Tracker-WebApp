__all__ = [
    "WEBAPP",
    "MongoDBType",
    "DatabaseType",
    "CollectionType",
    "CursorType",
]

from flask import Flask, Response, render_template, request, jsonify
from pymongo import database, collection, cursor
from pymongo import MongoClient
from typing import List, Any

from src.logger import *

MongoDBType = MongoClient[Any]
DatabaseType = database.Database[Any]
CollectionType = collection.Collection[Any]
CursorType = cursor.Cursor[Any]

WEBAPP = Flask(__name__)
client: MongoDBType = MongoClient("mongodb://localhost:27017/")
db: DatabaseType = client["presupuesto"]
gastos_collection: CollectionType = db["gastos"]

logger.info("API started.")
logger_specials.values_returned(WEBAPP, client, db, gastos_collection, init=__name__)


@WEBAPP.route("/")
def index() -> str:
    """
    index() Renders the index.html template and returns it as a string.

    @return The function index is returning a string representing the rendered index.html template.
    """
    logger_specials.was_called(__name__, index.__name__, key="debug")
    return render_template("index.html")


@WEBAPP.route("/gastos", methods=["GET"])
def get_gastos() -> Response:
    """
    get_gastos() Retrieves all gastos from the gastos_collection and returns them as a JSON response.

    @return The function get_gastos is returning a JSON response containing a list of gastos retrieved from the gastos_collection.
    """
    logger_specials.was_called(__name__, get_gastos.__name__, key="debug")

    gastos: List[CursorType] = list(gastos_collection.find())
    logger_specials.value_retured("gastos", gastos, get_gastos)

    return jsonify(gastos)


@WEBAPP.route("/gastos", methods=["POST"])
def add_gasto() -> Response:
    """
    add_gasto() Adds a new gasto to the gastos_collection based on the JSON data received in the request.

    @param gasto The gasto parameter in the add_gasto method is a JSON object representing the new gasto to be added to the gastos_collection.

    @return The function add_gasto is returning a JSON response with a success message upon successfully adding the gasto to the gastos_collection.
    """
    logger_specials.was_called(__name__, add_gasto.__name__, key="debug")

    gasto: Any | None = request.json
    logger_specials.value_retured("gasto", gasto, add_gasto)

    gastos_collection.insert_one(gasto)
    return jsonify({"message": "Gasto agregado correctamente"})


@WEBAPP.route("/gastos/<string:id>", methods=["PUT"])
def update_gasto(id: str) -> Response:
    """
    update_gasto(id) Updates an existing gasto in the gastos_collection with the provided ID based on the JSON data received in the request.

    @param id The id parameter in the update_gasto method is a string representing the ID of the gasto to be updated in the gastos_collection.
    @param updated_gasto The updated_gasto parameter in the update_gasto method is a JSON object representing the updated information of the gasto.

    @return The function update_gasto does not have a specific return value.
    """
    logger_specials.was_called(__name__, update_gasto.__name__)

    updated_gasto: Any | None = request.json
    logger_specials.value_retured("updated_gasto", updated_gasto, update_gasto)

    gastos_collection.update_one({"_id": id}, {"$set": updated_gasto})
    return jsonify({"message": "Gasto actualizado correctamente"})


@WEBAPP.route("/gastos/<string:id>", methods=["DELETE"])
def delete_gasto(id: str) -> Response:
    """
    delete_gasto(id) Deletes a gasto from the gastos_collection based on the provided ID.

    @param id The id parameter in the delete_gasto method is a string representing the ID of the gasto to be deleted from the gastos_collection.

    @return The function delete_gasto is returning a JSON response with a success message upon successfully deleting the gasto from the gastos_collection.
    """
    logger_specials.was_called(__name__, delete_gasto.__name__)
    gastos_collection.delete_one({"_id": id})
    return jsonify({"message": "Gasto eliminado correctamente"})
