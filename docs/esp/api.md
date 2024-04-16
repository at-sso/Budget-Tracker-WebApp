## Documentación de la API de Presupuesto

Este documento describe la API para una aplicación de gestión de presupuestos (presupuesto).

### Importaciones

El archivo `api/__init__.py` importa las bibliotecas necesarias para que la aplicación funcione.

- `Flask`: Un marco web para la construcción de aplicaciones web.
- `Response`: Se utiliza para crear respuestas a las solicitudes del cliente.
- `render_template`: Renderiza plantillas HTML.
- `request`: Accede a la información de la solicitud del cliente.
- `jsonify`: Convierte las estructuras de datos de Python a formato JSON para las respuestas.
- `pymongo`: Biblioteca para interactuar con bases de datos MongoDB.
- `MongoClient`: Clase para conectarse a un servidor MongoDB.
- `database`: Clase que representa una base de datos MongoDB.
- `collection`: Clase que representa una colección MongoDB.
- `cursor`: Clase que representa un cursor MongoDB.
- `typing`: Se utiliza para indicaciones de tipo.
- `logger`: Módulo de registro personalizado (implementación no proporcionada).

### Alias de tipos

El script define alias de tipos para las clases MongoDB de uso común para mejorar la legibilidad y el mantenimiento.

- `MongoDBType`: MongoClient
- `DatabaseType`: database.Database
- `CollectionType`: collection.Collection
- `CursorType`: cursor.Cursor

### Inicialización de la aplicación Flask

- `WEBAPP`: Se crea una instancia de aplicación Flask.
- `client`: Se crea una instancia de MongoClient para conectarse al servidor MongoDB en `mongodb://localhost:27017/`.
- `db`: Se conecta a la base de datos "presupuesto" en el servidor MongoDB.
- `gastos_collection`: Se conecta a la colección "gastos" dentro de la base de datos "presupuesto".
- `logger.info("API started.")`: Registra un mensaje indicando que la API se ha iniciado.
- `logger_specials.values_returned(WEBAPP, client, db, gastos_collection, init=__name__)`: Registra información sobre los componentes inicializados de la aplicación.

### Rutas disponibles

La API proporciona varias rutas para gestionar gastos (expensas) dentro de la aplicación de presupuesto.

- **`/` (GET)**:

  - Función: `index`
  - Descripción: Renderiza la plantilla `index.html`.
  - Devuelve: Una cadena que contiene la plantilla HTML renderizada.
  - Registro:
    - `logger_specials.was_called(__name__, index.__name__, key="debug")`: Registra un mensaje de depuración indicando que se ha llamado a la función `index`.

- **`/gastos` (GET)**:

  - Función: `get_gastos`
  - Descripción: Recupera todos los gastos de la `gastos_collection`.
  - Devuelve: Una respuesta JSON que contiene una lista de gastos recuperados.
  - Registro:
    - `logger_specials.was_called(__name__, get_gastos.__name__, key="debug")`: Registra un mensaje de depuración indicando que se ha llamado a la función `get_gastos`.
    - `logger_specials.value_retured("gastos", gastos, get_gastos)`: Registra información sobre los gastos recuperados.

- **`/gastos` (POST)**:

  - Función: `add_gasto`
  - Descripción: Añade un nuevo gasto a la `gastos_collection` basándose en los datos JSON proporcionados en el cuerpo de la solicitud.
  - Parámetro: `gasto` (JSON): Representa el nuevo gasto que se va a añadir.
  - Devuelve: Una respuesta JSON con un mensaje de éxito tras la adición correcta.
  - Registro:
    - `logger_specials.was_called(__name__, add_gasto.__name__, key="debug")`: Registra un mensaje de depuración indicando que se ha llamado a la función `add_gasto`.
    - `logger_specials.value_retured("gasto", gasto, add_gasto)`: Registra información sobre los datos del gasto recibido.

- **`/gastos/<string:id>` (PUT)**:

  - Función: `update_gasto`
  - Descripción: Actualiza un gasto existente en la `gastos_collection` con el ID proporcionado basándose en los datos JSON del cuerpo de la solicitud.
  - Parámetro: `id` (cadena): El ID del gasto que se va a actualizar.
  - Parámetro: `updated_gasto` (JSON): Representa la información actualizada del gasto.
  - Devuelve: Una respuesta JSON con un mensaje

- `/gastos/<string:id>` (DELETE)

  - **Función:** `delete_gasto`
  - **Descripción:** La función `delete_gasto` elimina un gasto (expense) de la colección `gastos` en base al ID proporcionado.
  - **Parámetro:** `id: str`: El ID del gasto que se va a eliminar.
  - **Devoluciones:** `Response`: Una respuesta JSON con un mensaje de éxito tras la eliminación correcta del gasto.
  - **Registro:**
    - `logger_specials.was_called(__name__, delete_gasto.__name__)`: Registra un mensaje indicando que se llamó a la función `delete_gasto`.
    - `gastos_collection.delete_one({"_id": id})`: Elimina el gasto de la colección `gastos`.
