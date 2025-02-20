const addTodo = () => {
    const todoText = todoInput.value;

    // Controlla se l'input non è vuoto
    if (!todoText.trim()) {
        alert('Please enter a task.');
        return;
    }

    // Crea un nuovo elemento li
    const todoItem = document.createElement('li');
    todoItem.classList.add('todo-item');

    // Crea uno span per il testo
    const todoTextElement = document.createElement('span');
    todoTextElement.innerText = todoText;

    // Crea un bottone per eliminare
    const deleteButton = document.createElement('button');
    deleteButton.classList.add('delete-button');
    deleteButton.innerText = 'Delete';

    // Aggiungi un evento per eliminare il TODO
    deleteButton.addEventListener('click', () => {
        todoList.removeChild(todoItem);
    });

    // Aggiungi il testo e il bottone all'elemento li
    todoItem.append(todoTextElement, deleteButton);

    // Aggiungi l'elemento li alla lista ul
    todoList.appendChild(todoItem);

    // Pulisci l'input
    todoInput.value = '';
};
