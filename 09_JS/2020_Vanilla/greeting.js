const form = document.querySelector(".js-form");
const input = form.querySelector("input");
const greeting = document.querySelector(".js-greetings");

const userName = "Current User";
const classShowing = "showing";

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
    
  } else {
    paintGreeting(currentUser);
  }
}

function init()
{
  loadName();
}

init();