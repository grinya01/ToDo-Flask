from flask import Flask, render_template, request, redirect
from flask_migrate import Migrate
from models import UserModel, TaskModel, db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
migrate = Migrate(app, db)
db.init_app(app)


@app.route('/create', methods=['GET', 'POST'])
def create_task():
    if request.method == 'GET':
        return render_template('create_task.html')

    if request.method == 'POST':
        task_name = request.form['content']
        task_description = request.form['description']
        task_owner = request.form['task_owner']
        new_task = TaskModel(task_name=task_name, description=task_description, task_owner=task_owner)
        print(new_task)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an error while adding the task'

    else:
        tasks = TaskModel.query.all()
        return render_template("home_page.html", tasks=tasks)


@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = TaskModel.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')

    except:
        return 'There was an error while deleting that task'


@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    task = TaskModel.query.get_or_404(id)

    if request.method == 'POST':
        task.task_name = request.form['task_name']
        task.description = request.form['description']

        try:
            db.session.commit()
            return redirect('/')

        except:
            return 'An error occurred while updating!'

    else:
        return render_template('update.html', task=task)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        new_user = UserModel(name=name, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect("http://127.0.0.1:5000/")


@app.route('/')
def home():
    tasks = TaskModel.query.all()
    return render_template("home_page.html", tasks=tasks)


if __name__ == '__main__':
    app.run(debug=True)