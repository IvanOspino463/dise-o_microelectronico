import re
from flask import Flask, render_template,request, redirect, url_for, flash


app = Flask(__name__)


@app.route('/')
def index():
    return 'Este es un mensaje'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        password = request.form['password']
        mail = request.form['mail']
        return render_template('login.html')
        




if __name__ == '__main__':
    app.run()
