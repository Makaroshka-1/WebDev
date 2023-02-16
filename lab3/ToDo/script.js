// Get references to HTML elements
const form = document.querySelector('#todo-form');
const input = document.querySelector('#todo-input');
const addButton = document.querySelector('#add-button');
const todoList = document.querySelector('#todo-list');


function addTodoItem(event) {
  
  event.preventDefault();


  const newTodo = input.value;

  if (newTodo.trim() === '') {
    alert('Please enter a to-do item');
    return;
  }
  const listItem = document.createElement('li');
  const checkbox = document.createElement('input');
  checkbox.type = 'checkbox';
  checkbox.classList.add('check');
  checkbox.addEventListener('click', toggleDone);
  const label = document.createElement('span');
  label.textContent = newTodo;
  const deleteButton = document.createElement('button');
  deleteButton.textContent = 'Delete';
  deleteButton.addEventListener('click', deleteTodoItem);

  listItem.appendChild(checkbox);
  listItem.appendChild(label);
  listItem.appendChild(deleteButton);

  todoList.appendChild(listItem);
  input.value = '';
}


function toggleDone(event) {
  const checkbox = event.target;
  const listItem = checkbox.parentNode;
  if (checkbox.checked) {
    listItem.classList.add('done');
  } else {
    listItem.classList.remove('done');
  }
}

function deleteTodoItem(event) {
  const deleteButton = event.target;
  const listItem = deleteButton.parentNode;
  todoList.removeChild(listItem);
}

addButton.addEventListener('click', addTodoItem);
