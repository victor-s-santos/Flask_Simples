from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return'<h1>Bem vindo ao Flask^^</h1>'

if __name__ == '__main__':
    app.run(debug=True)