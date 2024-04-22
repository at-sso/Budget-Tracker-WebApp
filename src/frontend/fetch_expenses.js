/*
 * The function `edit` is responsible for toggling the display of expense elements based on the provided `expense_id`.
 * If the element is currently hidden, it will be displayed, and vice versa.
 *
 * @param expense_id The `expense_id` parameter represents the unique identifier of the expense element to be edited.
 *
 * This function does not return any value.
 */
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
