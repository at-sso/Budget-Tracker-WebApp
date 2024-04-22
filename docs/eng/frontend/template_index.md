1. `<head>`: This section contains metadata about the document, such as the character encoding, viewport settings, and the title of the webpage.

2. `<meta charset="UTF-8" />`: Specifies the character encoding for the document as UTF-8, which supports a wide range of characters.

3. `<meta name="viewport" content="width=device-width, initial-scale=1.0" />`: Sets the viewport to the width of the device's screen at an initial scale of 1.

4. `<title>Expense Tracker</title>`: Sets the title of the webpage to "Expense Tracker".

5. `<link rel="stylesheet" href="/frontend/style.css" />`: Links an external stylesheet (`style.css`) located in the `/frontend` directory to style the HTML content.
   Let's break it down:

   ```css
   flex {
     display: flex;
   }
   ```

   This section defines a class called "flex" which sets the display property to "flex", allowing its children elements to be laid out in a flexible way either in a row or a column.

   ```css
   .btn {
     padding: 5px;
     cursor: pointer;
     height: fit-content;
     font-size: 14px;
   }
   ```

   The ".btn" class defines styles for buttons. It sets padding, cursor to a pointer when hovering, height to fit its content, and font size to 14 pixels.

   ```css
   .row {
     border: 1px solid #ddd;
     padding: 8px;
     text-align: left;
     justify-content: space-between;
   }
   ```

   The ".row" class defines styles for rows, typically used in a grid or table layout. It sets a border, padding, text alignment to the left, and justifies the content evenly along the row.

   ```css
   .row:not(.header) > span {
     border: 1px solid #ddd;
     padding: 8px;
     display: flex;
     align-items: center;
   }
   ```

   This part of the code defines styles for spans within rows that are not headers. It sets a border, padding, and aligns items to the center vertically.

   ```css
   .row span {
     width: 33%;
   }
   ```

   This sets the width of spans within rows to 33% of their container.

   ```css
   .header {
     text-align: center;
     background-color: #f2f2f2;
     font-weight: 600;
   }
   ```

   The ".header" class defines styles for header rows. It aligns text to the center, sets a background color, and increases the font weight.

   ```css
   body {
     font-family: Arial, sans-serif;
     margin: 0;
     padding: 20px;
   }
   ```

   This sets the font family for the entire document to Arial or a generic sans-serif font, with zero margin and 20 pixels of padding.

   ```css
   h1 {
     margin-bottom: 20px;
   }
   ```

   This adds a bottom margin of 20 pixels to all level 1 headings.

   ```css
   form {
     margin-bottom: 20px;
   }
   ```

   Forms will have a bottom margin of 20 pixels.

   ```css
   input[type="text"],
   input[type="number"] {
     padding: 8px;
     margin-right: 10px;
   }
   ```

   Text and number input fields will have 8 pixels of padding and a right margin of 10 pixels.

   ```css
   button {
     padding: 8px 16px;
     cursor: pointer;
   }
   ```

   Buttons will have 8 pixels of padding vertically and 16 pixels horizontally, and the cursor will change to a pointer on hover.

   ```css
   .expenses-table {
     border-collapse: collapse;
     width: 100%;
   }
   ```

This styles a table with class ".expenses-table" to collapse borders and occupy 100% width of its container.

1. `<body>`: The main content of the webpage begins here.

2. `<h1>Expense Tracker</h1>`: Displays the main heading of the webpage as "Expense Tracker".

3. `<h2>Add Expense</h2>`: Heading for the section where users can add new expenses.

4. `<form method="POST">`: Defines a form for submitting expense data using the POST method.

5. `{{form.hidden_tag()}} {{form.nombre(placeholder = "Nombre")}} {{form.monto(placeholder = "Monto")}} {{form.submit}}`: Inserts form fields for the expense name, amount, and a submit button. The `form.hidden_tag()` function generates hidden fields for CSRF protection.

6. `<h2>Expenses</h2>`: Heading for the section displaying existing expenses.

7. `<div class="expenses-table">`: Contains a table-like structure for displaying expenses.

8. `{% for gasto in gastos %}`: Initiates a loop over a list of expenses (`gastos`).

9. `<div class="row flex header">`: Defines a header row for the expense table.

10. `<span>Nombre</span> <span>Monto</span> <span>Fecha</span> <span style="width: 160px"></span>`: Defines column headers for the expense table (Name, Amount, Date) and an empty column for actions.

11. `{{editForm.hidden_tag()}} ... {{editForm.submit}}`: Inserts form fields for editing expenses within each expense row.

12. `<span> {{gasto["nombre"]}} </span> ...`: Displays the name, amount, and date of each expense within the expense row.

13. `<button onclick="edit('{{gasto._id}}')" class="{{gasto['_id']}} btn" type="button">cancelar</button>`: Defines a cancel button for editing an expense.

14. `<button onclick="edit('{{gasto._id}}')" class="btn">editar</button>`: Defines an edit button to edit an expense.

15. `<form method="POST"> {{deleteForm.hidden_tag()}} ... {{deleteForm.submit (class='btn')}} </form>`: Inserts a form for deleting an expense.

16. `</div>`: Closes the expense row.

17. `{% endfor %}`: Ends the loop over expenses.

18. `</div>`: Closes the expense table.

19. `<script src="/frontend/fetch_expenses.js"></script>`: Links an external JavaScript file (`fetch_expenses.js`) located in the `/frontend` directory to handle fetching expenses asynchronously.

[Go back](../index.md)
