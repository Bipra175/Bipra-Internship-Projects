from flask import Flask, jsonify, request

app = Flask(__name__)

# The list below stores all the tasks
tasks = [
    {"id": 1, "title": "Do homework", "done": False},
    {"id": 2, "title": "Clean the room", "done": True},
    {"id": 3, "title": "Buy groceries", "done": False},
    {"id": 4, "title": "Go for a walk", "done": False},
    {"id": 5, "title": "Read a book", "done": True}
]

# The function below will show all tasks
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# The function below will add a new task
@app.route('/api/tasks', methods=['POST'])
def add_task():
    new_task = request.get_json()
    new_task["id"] = len(tasks) + 1
    tasks.append(new_task)
    return jsonify({"message": "Task added", "task": new_task})

# The function below will update a task by its id
@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            data = request.get_json()
            task.update(data)
            return jsonify({"message": "Task updated", "task": task})
    return jsonify({"error": "Task not found"}), 404

# The function below will delete a task by its id
@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return jsonify({"message": "Task deleted"})
    return jsonify({"error": "Task not found"}), 404

# The main part will start the flask server
if __name__ == '__main__':
    app.run(debug=True)
