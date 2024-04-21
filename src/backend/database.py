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
    return datetime.now().strftime("%d/%m/%Y")


def registrar_gastos(nombre: str, monto: float) -> None:
    """Registrar un gasto en la base de datos."""
    date: str = __get_date()
    gasto: JSONType = {"nombre": nombre, "monto": monto, "fecha": date}
    collection_gastos.insert_one(gasto)
    logger.info(f"Gasto agregado: {gasto}")


def mostrar_gastos() -> List[JSONType]:
    """Obtener todos los gastos."""
    return list(collection_gastos.find())


def eliminar_gasto(id: str) -> None:
    """Eliminar un gasto."""
    collection_gastos.delete_one({"_id": id})
    logger.info(f"Gasto eliminado: {id}")


def modificar_gasto(id: str, nombre: str, monto: float) -> None:
    """Modificar un gasto existente."""
    date: str = __get_date()
    filtro: JSONType = {"_id": id}
    update_data: JSONType = {"$set": {"nombre": nombre, "monto": monto, "fecha": date}}
    collection_gastos.update_one(filtro, update_data)
    logger.info(f"Gasto modificado: {id}")
