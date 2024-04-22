1. **Imports and Definitions**:

   - It imports necessary modules such as `bson` for working with ObjectIds, `pymongo` for MongoDB interaction, and `datetime` for handling dates.
   - It defines custom types for MongoDB objects like `MongoDBType`, `DatabaseType`, and `CollectionType`.
   - It also defines `JSONType` as a dictionary with string keys and any value type.

2. **Connection Setup**:

   - It establishes a connection to a MongoDB instance running on `127.0.0.1` at port `27017`.
   - It defines a database named "presupuesto" (budget) and collections named "Gastos" (expenses) and "Ingresos" (incomes) within that database.

3. **Helper Function**:

   - `__get_date()`: Retrieves the current date in the format "dd/mm/yyyy".

4. **Expense Management Functions**:

   - `registrar_gastos(nombre: str, monto: float)`: Inserts a new expense into the "Gastos" collection along with the current date and logs the addition.
   - `mostrar_gastos()`: Retrieves all expenses from the "Gastos" collection and returns them as a list of JSON objects.
   - `eliminar_gasto(id: str)`: Deletes an expense from the "Gastos" collection based on its unique identifier.
   - `modificar_gasto(id: str, nombre: str, monto: float)`: Updates an existing expense in the "Gastos" collection with new information, including the current date.

5. **Documentation**:
   - Each function is documented using docstrings following the Google Python Style Guide, providing information on the purpose of the function and the parameters it accepts.

Overall, this module provides a set of functions to interact with a MongoDB database for managing budget-related data, specifically expenses.

[Go back](../index.md)
