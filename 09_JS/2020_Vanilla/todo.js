const toDoForm = document.querySelector(".js-toDoForm");
const toDoInput = toDoForm.querySelector("input");
const toDoList = document.querySelector(".js-toDoList");

const toDos = [];

function saveToDo(text)
{
  const toDo = document.createElement("li");
  const delButton = document.createElement("button");
  delButton.innerHTML = "❌";
  const span = document.createElement("span");
  span.innerText = text;
  toDo.appendChild(span);
  toDo.appendChild(delButton);
  toDoList.appendChild(toDo);
}

function toDoSubmit(event)
{
  event.preventDefault();
  const inputValue = toDoInput.value;
  toDoInput.value = "";
  saveToDo(inputValue);  
}

function loadToDos()
{
  const currentTodos = localStorage.getItem("toDos");
  if (currentTodos !== null)
  {
    localStorage.setItem("toDos", toDos);
  }
}

function init() {
  loadToDos();
  toDoForm.addEventListener("submit", toDoSubmit);
}

init();