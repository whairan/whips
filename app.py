from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

# Simulating a database with a list of dictionaries
todos = [
    {"id": 1, "task": "Read a book", "done": False},
    {"id": 2, "task": "Write some code", "done": False}
]

# HTML template embedded in Python for simplicity
HTML = """
<!doctype html>
<title>Todo List</title>
<h1>Todo List</h1>
<form action="/" method="POST">
    <input type="text" name="task" placeholder="Add new task">
    <button type="submit">Add</button>
</form>
<ul>
    {% for todo in todos %}
        <li>
            {{ todo.task }}
            {% if not todo.done %}
                <a href="/done/{{ todo.id }}">Mark as done</a>
            {% else %}
                <span style="color: green;">Done!</span>
            {% endif %}
            <a href="/delete/{{ todo.id }}">Delete</a>
        </li>
    {% endfor %}
</ul>
"""

@app.route('/', methods=['GET', 'POST'])
def todo_list():
    if request.method == 'POST':
        # Add new task
        new_id = max(todo['id'] for todo in todos) + 1 if todos else 1
        new_task = request.form['task']
        todos.append({"id": new_id, "task": new_task, "done": False})
        return redirect(url_for('todo_list'))
    return render_template_string(HTML, todos=todos)

@app.route('/done/<int:todo_id>')
def mark_as_done(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            todo['done'] = True
            break
    return redirect(url_for('todo_list'))

@app.route('/delete/<int:todo_id>')
def delete_task(todo_id):
    global todos
    todos = [todo for todo in todos if todo['id'] != todo_id]
    return redirect(url_for('todo_list'))

if __name__ == '__main__':
    app.run(debug=True)

