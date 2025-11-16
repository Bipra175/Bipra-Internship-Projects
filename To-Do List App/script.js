const input = document.getElementById("taskInput");
const addBtn = document.getElementById("addBtn");
const list = document.getElementById("taskList");

document.addEventListener("DOMContentLoaded", loadTasks);
addBtn.addEventListener("click", addTask);

function addTask() {
  if (input.value.trim() === "") return alert("Enter a task!");
  const li = createTask(input.value);
  list.appendChild(li);
  saveData();
  input.value = "";
}

function createTask(text) {
  const li = document.createElement("li");
  li.textContent = text;

  li.addEventListener("click", () => {
    li.classList.toggle("completed");
    saveData();
  });

  const del = document.createElement("button");
  del.textContent = "Delete";
  del.className = "delete";
  del.onclick = () => { li.remove(); saveData(); };

  li.appendChild(del);
  return li;
}

function saveData() {
  const tasks = [];
  document.querySelectorAll("#taskList li").forEach(li => {
    tasks.push({
      text: li.firstChild.textContent,
      completed: li.classList.contains("completed")
    });
  });
  localStorage.setItem("tasks", JSON.stringify(tasks));
}

function loadTasks() {
  const tasks = JSON.parse(localStorage.getItem("tasks")) || [];
  tasks.forEach(t => {
    const li = createTask(t.text);
    if (t.completed) li.classList.add("completed");
    list.appendChild(li);
  });
}
