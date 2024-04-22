// Function to fetch expenses from server and populate the table
function edit(expense_id) {
  if (
    document.getElementsByClassName(expense_id)[1].getAttribute("type") ==
    "hidden"
  ) {
    document.getElementsByClassName(expense_id)[0].style.display = "flex";
    document.getElementsByClassName(expense_id)[1].setAttribute("type", "");
    document.getElementsByClassName(expense_id)[2].setAttribute("type", "");
    document.getElementsByClassName(expense_id)[3].style.display = "block";
    document.getElementsByClassName(expense_id)[4].style.display = "none";
    document.getElementsByName(expense_id)[0].style.display = "none";
    document.getElementsByName(expense_id)[1].style.display = "none";
    document.getElementsByName(expense_id)[2].style.display = "none";
  } else {
    document.getElementsByClassName(expense_id)[0].style.display = "none";
    document
      .getElementsByClassName(expense_id)[1]
      .setAttribute("type", "hidden");
    document
      .getElementsByClassName(expense_id)[2]
      .setAttribute("type", "hidden");
    document.getElementsByClassName(expense_id)[3].style.display = "none";
    document.getElementsByClassName(expense_id)[4].style.display = "flex";

    document.getElementsByName(expense_id)[0].style.display = "flex";
    document.getElementsByName(expense_id)[1].style.display = "flex";
    document.getElementsByName(expense_id)[2].style.display = "flex";
  }
}

// Function to handle form submission for adding expenses
