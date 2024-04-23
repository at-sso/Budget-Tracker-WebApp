1. `<head>`: Esta sección contiene metadatos sobre el documento, como la codificación de caracteres, configuraciones de viewport y el título de la página web.

2. `<meta charset="UTF-8" />`: Especifica la codificación de caracteres del documento como UTF-8, que admite una amplia gama de caracteres.

3. `<meta name="viewport" content="width=device-width, initial-scale=1.0" />`: Establece el viewport al ancho de la pantalla del dispositivo con una escala inicial de 1.

4. `<title>Expense Tracker</title>`: Establece el título de la página web como "Expense Tracker".

5. `<link rel="stylesheet" href="/frontend/style.css" />`: Enlaza una hoja de estilo externa (`style.css`) ubicada en el directorio `/frontend` para estilizar el contenido HTML.
   Desglosemos:

   ```css
   flex {
     display: flex;
   }
   ```

   Esta sección define una clase llamada "flex" que establece la propiedad de visualización en "flex", permitiendo que sus elementos hijos se distribuyan de manera flexible ya sea en fila o columna.

   ```css
   .btn {
     padding: 5px;
     cursor: pointer;
     height: fit-content;
     font-size: 14px;
   }
   ```

   La clase ".btn" define estilos para botones. Establece el relleno, el cursor como puntero al pasar el mouse, la altura para ajustarse a su contenido y el tamaño de fuente a 14 píxeles.

   ```css
   .row {
     border: 1px solid #ddd;
     padding: 8px;
     text-align: left;
     justify-content: space-between;
   }
   ```

   La clase ".row" define estilos para filas, típicamente utilizadas en una disposición de cuadrícula o tabla. Establece un borde, relleno, alineación de texto a la izquierda y justifica el contenido uniformemente a lo largo de la fila.

   ```css
   .row:not(.header) > span {
     border: 1px solid #ddd;
     padding: 8px;
     display: flex;
     align-items: center;
   }
   ```

   Esta parte del código define estilos para spans dentro de filas que no son encabezados. Establece un borde, relleno y alinea los elementos al centro verticalmente.

   ```css
   .row span {
     width: 33%;
   }
   ```

   Esto establece el ancho de spans dentro de filas en un 33% de su contenedor.

   ```css
   .header {
     text-align: center;
     background-color: #f2f2f2;
     font-weight: 600;
   }
   ```

   La clase ".header" define estilos para filas de encabezado. Alinea el texto al centro, establece un color de fondo y aumenta el peso de la fuente.

   ```css
   body {
     font-family: Arial, sans-serif;
     margin: 0;
     padding: 20px;
   }
   ```

   Esto establece la familia de fuentes para todo el documento en Arial o una fuente sans-serif genérica, sin margen y con un relleno de 20 píxeles.

   ```css
   h1 {
     margin-bottom: 20px;
   }
   ```

   Esto agrega un margen inferior de 20 píxeles a todos los encabezados de nivel 1.

   ```css
   form {
     margin-bottom: 20px;
   }
   ```

   Los formularios tendrán un margen inferior de 20 píxeles.

   ```css
   input[type="text"],
   input[type="number"] {
     padding: 8px;
     margin-right: 10px;
   }
   ```

   Los campos de entrada de texto y número tendrán 8 píxeles de relleno y un margen derecho de 10 píxeles.

   ```css
   button {
     padding: 8px 16px;
     cursor: pointer;
   }
   ```

   Los botones tendrán 8 píxeles de relleno vertical y 16 píxeles horizontalmente, y el cursor cambiará a un puntero al pasar el mouse.

   ```css
   .expenses-table {
     border-collapse: collapse;
     width: 100%;
   }
   ```

   Esto aplica estilos a una tabla con la clase ".expenses-table" para colapsar bordes y ocupar el 100% del ancho de su contenedor.

6. `<body>`: El contenido principal de la página web comienza aquí.

7. `<h1>Expense Tracker</h1>`: Muestra el encabezado principal de la página web como "Expense Tracker".

8. `<h2>Add Expense</h2>`: Encabezado para la sección donde los usuarios pueden agregar nuevos gastos.

9. `<form method="POST">`: Define un formulario para enviar datos de gastos utilizando el método POST.

10. `{{form.hidden_tag()}} {{form.nombre(placeholder = "Nombre")}} {{form.monto(placeholder = "Monto")}} {{form.submit}}`: Inserta campos de formulario para el nombre del gasto, el monto y un botón de envío. La función `form.hidden_tag()` genera campos ocultos para la protección CSRF.

11. `<h2>Expenses</h2>`: Encabezado para la sección que muestra los gastos existentes.

12. `<div class="expenses-table">`: Contiene una estructura similar a una tabla para mostrar los gastos.

13. `{% for gasto in gastos %}`: Inicia un bucle sobre una lista de gastos (`gastos`).

14. `<div class="row flex header">`: Define una fila de encabezado para la tabla de gastos.

15. `<span>Nombre</span> <span>Monto</span> <span>Fecha</span> <span style="width: 160px"></span>`: Define encabezados de columna para la tabla de gastos (Nombre, Monto, Fecha) y una columna vacía para acciones.

16. `{{editForm.hidden_tag()}} ... {{editForm.submit}}`: Inserta campos de formulario para editar gastos dentro de cada fila de gasto.

17. `<span> {{gasto["nombre"]}} </span> ...`: Muestra el nombre, monto y fecha de cada gasto dentro de la fila de gasto.

18. `<button onclick="edit('{{gasto._id}}')" class="{{gasto['_id']}} btn" type="button">cancelar</button>`: Define un botón de cancelar para editar un gasto.

19. `<button onclick="edit('{{gasto._id}}')" class="btn">editar</button>`: Define un botón de edición para editar un gasto.

20. `<form method

="POST"> {{deleteForm.hidden_tag()}} ... {{deleteForm.submit (class='btn')}} </form>`: Inserta un formulario para eliminar un gasto.

16. `</div>`: Cierra la fila de gasto.

17. `{% endfor %}`: Finaliza el bucle sobre los gastos.

18. `</div>`: Cierra la tabla de gastos.

19. `<script src="/frontend/fetch_expenses.js"></script>`: Enlaza un archivo JavaScript externo (`fetch_expenses.js`) ubicado en el directorio `/frontend` para manejar la obtención de gastos de forma asíncrona.

[Ir atrás](../index.md)
