from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='../templates')
todos = []

@app.route('/')
def home():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('todo')
    if task:
        todos.append({'id': len(todos), 'task': task, 'done': False})
    return redirect(url_for('home'))

@app.route('/toggle/<int:id>', methods=['POST'])
def toggle(id):
    if 0 <= id < len(todos):
        todos[id]['done'] = not todos[id]['done']
    return redirect(url_for('home'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'POST':
        task = request.form.get('task')
        if task and 0 <= id < len(todos):
            todos[id]['task'] = task
        return redirect(url_for('home'))
    return render_template('edit.html', todo=todos[id] if 0 <= id < len(todos) else None)

@app.route('/delete/<int:id>')
def delete(id):
    if 0 <= id < len(todos):
        todos.pop(id)
        # Re-index todos
        for i, todo in enumerate(todos):
            todo['id'] = i
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)