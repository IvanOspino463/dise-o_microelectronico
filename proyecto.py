from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return 'Este es un mensaje de prueba.'


if __name__ == '__main__':
    app.run()
