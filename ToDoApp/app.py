from flask import Flask,render_template,request,redirect,url_for



#app instance from the Flask class

app =   Flask(__name__,template_folder='templates')


tasks = []

@app.route('/')
def home():
    return render_template('index.html',tasks=tasks)


@app.route('/add',methods=['POST','GET'])
def create_new_task():
    task = request.form.get('task')
    tasks.append(task)
    return redirect(url_for('home'))


@app.route('/delete/<int:index>')
def delete_task(index):
    if 0 <= index < len(tasks):
        del tasks[index]
    return redirect(url_for('home'))    

#update task name 
@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit_task(index):
    if 0 <= index < len(tasks):
        if request.method == 'POST':
            updated_task = request.form.get('task')
            tasks[index] = updated_task  # Update the task in the list
            return redirect(url_for('home'))
        task_to_edit = tasks[index]  # Get the task to be edited
        return render_template('edit_task.html', task=task_to_edit, index=index)
    return redirect(url_for('home'))  # In case of an invalid index



if __name__ == '__main__':
    app.run(debug=True)