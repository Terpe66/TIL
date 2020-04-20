const init = () => {
    const todoBox = document.querySelector("#todo_box");
    const reverseButton = document.querySelector("#reverse_btn");
    const fetchButton = document.querySelector("#fetch_btn");
// TODO: input, Add 버튼에 createTodo와 이벤트 리스너 버무리기

    fetchButton.addEventListener("click", e => {
        fetchData("https://koreanjson.com/todos/");
    });
    reverseButton.addEventListener("click", e => {
        reverseTodos()
    });
// TODO: 버튼 만들고, 데이터 받아오게 이벤트 리스너 클릭

    const fetchData = URL => {
        fetch(URL)
            .then(res => res.json())
            .then(todos => {
                for (const todo of todos) {
                    todoBox.appendChild(createTodo(todo.title, todo.completed));
                }
            })
    };

    const createTodo = (inputText, completed = false) => {
        // let completed = false;
        // Card 만들기
        const todoCard = document.createElement("div");
        todoCard.classList.add("ui", "segment", "todo-item");
        if (completed) todoCard.classList.add("secondary");

// if (completed) {
//     todoCard.className = "ui secondary segment todo-item";
// } else {
//     todoCard.className = "ui segment todo-item";
// }
// todoCard.classList.add(completed ? "secondary" : "");
// todoCard.className = "ui segment todo-item";
// todoCard.className += completed ? "secondary" : "";

        // Card > Wrapper
        const wrapper = document.createElement("div");
        wrapper.classList.add("ui", "checkbox");
        // Card > Wrapper > input (checkbox)
        const input = document.createElement("input");
        input.setAttribute("type", "checkbox");
        input.checked = completed;

        input.addEventListener("click", e => {
            if (input.checked) {
                label.classList.add("completed-label");
                todoCard.classList.add("secondary");
            } else {
                label.classList.remove("completed-label");
                todoCard.classList.remove("secondary");
            }
            completed = !completed;
        });
        // Card > Wrapper > label (text)
        const label = document.createElement("label");
        label.innerHTML = inputText;
        if (completed) label.classList.add("completed-label");
// label.classList.add(completed ? "completed-label" : "");
// label.style = completed ? "text-decoration: line-through" : "text-decoration: none";

        const deleteIcon = document.createElement("i"); // <i> </i>
        deleteIcon.classList.add("close", "icon", "delete-icon"); // <i class="close icon"></i>

        deleteIcon.addEventListener("click", e => {
            todoBox.removeChild(todoCard);
        });

        wrapper.appendChild(input);
        wrapper.appendChild(label);
        todoCard.appendChild(wrapper);
        todoCard.appendChild(deleteIcon);

        return todoCard
    };

    const reverseTodos = () => {
        const allTodos = Array.from(document.querySelectorAll(".todo-item"));

        while (todoBox.firstChild) {
            todoBox.removeChild(todoBox.firstChild)
        }

        for (const todo of allTodos.reverse()) {
            todoBox.appendChild(todo);
        }
    }

    todoBox.appendChild(createTodo("JS", true));
};
init();

