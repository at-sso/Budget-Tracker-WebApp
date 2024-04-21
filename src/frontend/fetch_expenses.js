// Function to fetch expenses from server and populate the table
function fetchExpenses() {
  fetch("/expenses")
    .then((response) => response.json())
    .then((data) => {
      const expenseTableBody = document.querySelector("#expenseTable tbody");
      expenseTableBody.innerHTML = "";
      data.forEach((expense) => {
        const row = document.createElement("tr");
        row.innerHTML = `
                            <td>${expense.nombre}</td>
                            <td>${expense.monto}</td>
                            <td>${expense.fecha}</td>
                        `;
        expenseTableBody.appendChild(row);
      });
    });
}

// Function to handle form submission for adding expenses
document
  .getElementById("expenseForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();
    const nombre = document.getElementById("nombre").value;
    const monto = document.getElementById("monto").value;
    fetch("/expenses", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ nombre, monto }),
    }).then((response) => {
      if (response.ok) {
        fetchExpenses(); // Fetch and update table if expense added successfully
        document.getElementById("nombre").value = "";
        document.getElementById("monto").value = "";
      }
    });
  });

// Fetch expenses when page loads
fetchExpenses();
