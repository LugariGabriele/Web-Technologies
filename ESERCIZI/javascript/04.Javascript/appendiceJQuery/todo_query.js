// Aspetta che il DOM sia pronto
$(document).ready(function() {
    // Aggiungi un evento al click del pulsante "Add"
    $('#todo-button').on('click', function() {
        // Ottieni il valore dell'input
        var todoText = $('#todo-input').val();

        // Controlla se l'input non è vuoto
        if (todoText === '') {
            alert('Please enter a task.');
            return;
        }

        // Crea un nuovo elemento li con il testo e il bottone di delete
        var todoItem = $('<li class="todo-item"></li>');
        var todoTextElement = $('<span></span>').text(todoText);
        var deleteButton = $('<button class="delete-button">Delete</button>');

        // Aggiungi un evento per eliminare il TODO
        deleteButton.on('click', function() {
            todoItem.remove(); // Rimuovi l'elemento dalla lista
        });

        // Aggiungi il testo e il bottone all'elemento li
        todoItem.append(todoTextElement).append(deleteButton);

        // Aggiungi l'elemento li alla lista ul
        $('#todo-list').append(todoItem);

        // Pulisci l'input
        $('#todo-input').val('');
    });
});
