from flask import Flask, render_template, request
from wtforms import Form

class MenuForm(Form):
    menuRadio = RadioField('Menu', choices=[('ver','vertical'),('hor','horizontal')])

app = Flask(__name__)



@app.route('/')
def hello():
    return render_template("index.html", form=MenuForm(), adr = "menu")

@app.route('/menu', methods=["GET", "POST"])
def editDataByAdmin():
    login = request.form['login']


if __name__ == '__main__':
    app.run(debug=True)