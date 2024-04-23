1. **Importaciones y Definiciones:**
- Importa módulos necesarios como `bson` para trabajar con `ObjectIds`, `pymongo` para la interacción con MongoDB y `datetime` para manejar fechas.
- Define tipos personalizados para objetos de MongoDB como `MongoDBType`, `DatabaseType` y `CollectionType`.
- También define `JSONType` como un diccionario con claves de tipo string y cualquier valor.

2. **Configuración de la Conexión:**

- Establece una conexión a una instancia de MongoDB que se está ejecutando en `127.0.0.1 `en el puerto `27017`.
- Define una base de datos llamada "presupuesto" y colecciones llamadas "Gastos" e "Ingresos" dentro de esa base de datos.

3. **Función Auxiliar:**

- `__get_date()`: Obtiene la fecha actual en el formato `"dd/mm/yyyy"`.

4. **Funciones de Gestión de Gastos:**

- `registrar_gastos(nombre: str, monto: float)`: Inserta un nuevo gasto en la colección "Gastos" junto con la fecha actual y registra la adición.
- `mostrar_gastos()`: Obtiene todos los gastos de la colección "Gastos" y los devuelve como una lista de objetos JSON.
- `eliminar_gasto(id: str)`: Elimina un gasto de la colección "Gastos" basado en su identificador único.
- `modificar_gasto(id: str, nombre: str, monto: float)`: Actualiza un gasto existente en la colección "Gastos" con nueva información, incluyendo la fecha actual.

5. **Documentación:**

- Cada función está documentada utilizando docstrings siguiendo la Guía de Estilo de Python de Google, proporcionando información sobre el propósito de la función y los parámetros que acepta.


En general, este módulo proporciona un conjunto de funciones para interactuar con una base de datos MongoDB para gestionar datos relacionados con el presupuesto, específicamente los gastos.

[Ir atrás](../index.md)




