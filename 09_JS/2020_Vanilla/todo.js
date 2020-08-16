const toDoForm = document.querySelector(".js-toDoForm");
const toDoInput = toDoForm.querySelector("input");
const toDoList = document.querySelector(".js-toDoList");

let toDos = [];

function deleteToDo(event)
{
  const button = event.target;
  const li = button.parentNode;
  toDoList.removeChild(li);
  toDos = toDos.filter(function (toDo)
  {
    return toDo.id !== parseInt(li.id);
  })
  toStorage();
}

function toStorage()
{
  localStorage.setItem("toDos", JSON.stringify(toDos));
}

function saveToDo(text)
{
  const toDo = document.createElement("li");
  const delButton = document.createElement("button");
  delButton.innerHTML = "❌";
  delButton.addEventListener("click", deleteToDo);
  const span = document.createElement("span");
  let idx = 1;
  if (toDos.length !== 0)
  {
    idx = toDos[toDos.length - 1].id + 1;
  }
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
  toStorage();
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