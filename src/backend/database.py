__all__ = [
    # Types:
    "MongoDBType",
    "DatabaseType",
    "CollectionType",
    "JSONType",
    # Variables:
    "collection_gastos",
    "collection_ingresos",
    # Functions:
    "registrar_gastos",
    "mostrar_gastos",
    "eliminar_gasto",
    "modificar_gasto",
]

from bson import ObjectId
from pymongo.database import Database
from pymongo.collection import Collection
from pymongo import MongoClient
from datetime import datetime
from typing import (
    Any,
    Dict,
    List,
)

from .logger import *

MongoDBType = MongoClient[Any]
DatabaseType = Database[Any]  # type: ignore[misc]
CollectionType = Collection[Any]  # type: ignore[misc]
JSONType = Dict[str, Any] | Any

# Conexión a MongoDB
client: MongoDBType = MongoClient("mongodb://127.0.0.1:27017/")
# Nombre de la base de datos
database: DatabaseType = client["presupuesto"]
# Colección de gastos
collection_gastos: CollectionType = database["Gastos"]
collection_ingresos: CollectionType = database["Ingresos"]


def __get_date() -> str:
    """
    The function `__get_date` retrieves the current date in the format "dd/mm/yyyy".

    @return The function `__get_date` returns a string representing the current date in the format "dd/mm/yyyy".
    """
    return datetime.now().strftime("%d/%m/%Y")


def registrar_gastos(nombre: str, monto: float) -> None:
    """
    The function `registrar_gastos` registers a new expense by inserting it into a collection, logging
    the addition of the expense.

    @param nombre The `nombre` parameter in the `registrar_gastos` function is a string representing
    the name of the expense to be registered.
    @param monto The `monto` parameter in the `registrar_gastos` function is a float representing the
    amount of the expense to be registered.
    """
    date: str = __get_date()
    gasto: JSONType = {"nombre": nombre, "monto": monto, "fecha": date}
    collection_gastos.insert_one(gasto)
    logger.info(f"Gasto agregado: {gasto}")


def mostrar_gastos() -> List[JSONType]:
    """
    The function `mostrar_gastos` retrieves and returns a list of all expenses stored in a collection.

    @return The function `mostrar_gastos` returns a list of JSON objects representing the expenses
    stored in the collection.
    """
    return list(collection_gastos.find())


def eliminar_gasto(id: str) -> None:
    """
    The function `eliminar_gasto` removes an expense from the collection based on its unique identifier.

    @param id The `id` parameter in the `eliminar_gasto` function is a string representing the unique
    identifier of the expense to be deleted.
    """
    (collection_gastos.delete_one({"_id": ObjectId(id)}))
    logger.info(f"Gasto eliminado: {id}")


def modificar_gasto(id: str, nombre: str, monto: float) -> None:
    """
    The function `modificar_gasto` updates an existing expense in the collection with new information.

    @param id The `id` parameter in the `modificar_gasto` function is a string representing the unique
    identifier of the expense to be modified.
    @param nombre The `nombre` parameter in the `modificar_gasto` function is a string representing the
    new name of the expense.
    @param monto The `monto` parameter in the `modificar_gasto` function is a float representing the new
    amount of the expense.
    """
    date: str = __get_date()
    filtro: JSONType = {"_id": ObjectId(id)}
    update_data: JSONType = {"$set": {"nombre": nombre, "monto": monto, "fecha": date}}
    logger.debug(collection_gastos.update_one(filtro, update_data))
    logger.info(f"Gasto modificado: {id}")
