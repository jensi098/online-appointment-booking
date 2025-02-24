from flask import Flask, render_template, request, redirect, url_for

app = Flask(_name_)
appointments = []  # Temporary in-memory storage

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        appointment = {
            "name": request.form['name'],
            "contact": request.form['contact'],
            "date": request.form['date'],
            "time": request.form['time'],
            "service_type": request.form['service_type']
        }
        appointments.append(appointment)
        return redirect(url_for('index'))

    return render_template('index.html', appointments=appointments)

if _name_ == '_main_':
    app.run(debug=True)
