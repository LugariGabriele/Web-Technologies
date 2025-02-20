// Seleziona gli elementi dall'HTML
var todoInput = document.getElementById('todo-input');
var todoButton = document.getElementById('todo-button');
var todoList = document.getElementById('todo-list');

// Aggiungi un ascoltatore per il clic del bottone
todoButton.addEventListener('click', addTodo);

// Funzione per aggiungere un TODO
function addTodo() {
    var todoText = todoInput.value;

    // Controlla se l'input non è vuoto
    if (todoText === '') {
        alert('Please enter a task.');
        return;
    }

    // Crea un nuovo elemento li
    var todoItem = document.createElement('li');
    todoItem.className = 'todo-item';

    // Crea uno span per il testo
    var todoTextElement = document.createElement('span');
    todoTextElement.innerText = todoText;

    // Crea un bottone per eliminare
    var deleteButton = document.createElement('button');
    deleteButton.className = 'delete-button';
    deleteButton.innerText = 'Delete';

    // Aggiungi un evento per eliminare il TODO
    deleteButton.addEventListener('click', function() {
        todoList.removeChild(todoItem);
    });

    // Aggiungi il testo e il bottone all'elemento li
    todoItem.appendChild(todoTextElement);
    todoItem.appendChild(deleteButton);

    // Aggiungi l'elemento li alla lista ul
    todoList.appendChild(todoItem);

    // Pulisci l'input
    todoInput.value = '';
}
