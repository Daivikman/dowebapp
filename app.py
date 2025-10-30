from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    todo = request.form.get('todo')
    if todo:
        todos.append({'id': len(todos) + 1, 'task': todo, 'done': False})
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    todo = next((t for t in todos if t['id'] == id), None)
    if request.method == 'POST':
        new_task = request.form.get('todo')
        if todo and new_task:
            todo['task'] = new_task
        return redirect(url_for('index'))
    return render_template('edit.html', todo=todo)

@app.route('/delete/<int:id>')
def delete(id):
    global todos
    todos = [t for t in todos if t['id'] != id]
    return redirect(url_for('index'))

@app.route('/toggle/<int:id>', methods=['POST'])
def toggle(id):
    todo = next((t for t in todos if t['id'] == id), None)
    if todo:
        todo['done'] = not todo['done']
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)