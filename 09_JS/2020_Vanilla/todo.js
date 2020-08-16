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
  const idx = toDos.length + 1;
  span.innerText = text;
  toDo.appendChild(span);
  toDo.appendChild(delButton);
  toDo.id = idx;
  toDoList.appendChild(toDo);
  const toDoObj = {
    text: text,
    id: idx
  }
  toDos.push(toDoObj);
  localStorage.setItem("toDos", JSON.stringify(toDos));
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
    const parsedTodos = JSON.parse(currentTodos);
    parsedTodos.forEach(function (toDo)
    {
      saveToDo(toDo.text);
    })
  }
}

function init() {
  loadToDos();
  toDoForm.addEventListener("submit", toDoSubmit);
}

init();