const form = document.querySelector(".js-form");
const input = form.querySelector("input");
const greeting = document.querySelector(".js-greetings");

const classShowing = "showing";

function checkSubmit(event)
{
  event.preventDefault();
  const inputName = input.value;
  saveName(inputName);
  paintGreeting(inputName);
}

function saveName(inputName)
{
  localStorage.setItem("username", inputName);
}

function getName()
{
  form.classList.add(classShowing);
  form.addEventListener("submit", checkSubmit)
}

function paintGreeting(text)
{
  form.classList.remove(classShowing);
  greeting.classList.add(classShowing);
  greeting.innerText = `Hello ${text}`;
}

function loadName()
{
  const currentUser = localStorage.getItem("username");
  if (currentUser === null)
  {
    getName();
  } else {
    paintGreeting(currentUser);
  }
}

function init()
{
  loadName();
}

init();