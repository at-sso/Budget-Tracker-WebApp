## API

This document describes the API for a presupuesto (budget) management.

### Imports

The `api/__init__.py` file imports the necessary libraries for the application to function.

- `Flask`: A web framework for building web applications.
- `Response`: Used to create responses to client requests.
- `render_template`: Renders HTML templates.
- `request`: Accesses information from the client request.
- `jsonify`: Converts Python data structures to JSON format for responses.
- `pymongo`: Library for interacting with MongoDB databases.
- `MongoClient`: Class for connecting to a MongoDB server.
- `database`: Class representing a MongoDB database.
- `collection`: Class representing a MongoDB collection.
- `cursor`: Class representing a MongoDB cursor.
- `typing`: Used for type hints.
- `logger`: Custom logger module (implementation not provided).

### Type Aliases

The script defines type aliases for commonly used MongoDB classes to improve readability and maintainability.

- `MongoDBType`: MongoClient
- `DatabaseType`: database.Database
- `CollectionType`: collection.Collection
- `CursorType`: cursor.Cursor

### Flask App Initialization

- `WEBAPP`: A Flask application instance is created.
- `client`: A MongoClient instance is created to connect to the MongoDB server at `mongodb://localhost:27017/`.
- `db`: Connects to the "presupuesto" database on the MongoDB server.
- `gastos_collection`: Connects to the "gastos" collection within the "presupuesto" database.
- `logger.info("API started.")`: Logs a message indicating the API has started.
- `logger_specials.values_returned(WEBAPP, client, db, gastos_collection, init=__name__)`: Logs information about the initialized application components.

### Available Routes

The API provides several routes for managing gastos (expenses) within the presupuesto (budget) application.

- **`/` (GET)**:

  - Function: `index`
  - Description: Renders the `index.html` template.
  - Returns: A string containing the rendered HTML template.
  - Logging:
    - `logger_specials.was_called(__name__, index.__name__, key="debug")`: Logs a debug message indicating the `index` function was called.

- **`/gastos` (GET)**:

  - Function: `get_gastos`
  - Description: Retrieves all gastos from the `gastos_collection`.
  - Returns: A JSON response containing a list of retrieved gastos.
  - Logging:
    - `logger_specials.was_called(__name__, get_gastos.__name__, key="debug")`: Logs a debug message indicating the `get_gastos` function was called.
    - `logger_specials.value_retured("gastos", gastos, get_gastos)`: Logs information about the retrieved gastos.

- **`/gastos` (POST)**:

  - Function: `add_gasto`
  - Description: Adds a new gasto to the `gastos_collection` based on the provided JSON data in the request body.
  - Parameter: `gasto` (JSON): Represents the new gasto to be added.
  - Returns: A JSON response with a success message upon successful addition.
  - Logging:
    - `logger_specials.was_called(__name__, add_gasto.__name__, key="debug")`: Logs a debug message indicating the `add_gasto` function was called.
    - `logger_specials.value_retured("gasto", gasto, add_gasto)`: Logs information about the received gasto data.

- **`/gastos/<string:id>` (PUT)**:

  - Function: `update_gasto`
  - Description: Updates an existing gasto in the `gastos_collection` with the provided ID based on the JSON data in the request body.
  - Parameter: `id` (string): The ID of the gasto to be updated.
  - Parameter: `updated_gasto` (JSON): Represents the updated information for the gasto.
  - Returns: A JSON response with a success message upon successful update.
  - Logging:
    - `logger_specials.was_called(__name__, update_gasto.__name__)`: Logs a message indicating the `update_gasto` function was called.
    - `logger_specials.value_retured("updated_gasto", updated_gasto, update_gasto)`: Logs information about the received updated gasto data.

- **`/gastos/<string:id>` (DELETE)**:
  - Function: `delete
  - Description: The `delete_gasto` function removes a gasto (expense) from the `gastos_collection` based on the provided ID.
  - Parameter: `id: str`: The ID of the gasto to be deleted.
  - Returns: `Response`: A JSON response with a success message upon successful deletion of the gasto.
  - Logging:
    - `logger_specials.was_called(__name__, delete_gasto.__name__)`: Logs a message indicating the `delete_gasto` function was called.
    - `gastos_collection.delete_one({"_id": id})`: Deletes the gasto from the `gastos_collection`.
