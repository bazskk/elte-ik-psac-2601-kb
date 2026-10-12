from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello from Flask!</h1><br><p>Hello World!</p>'


if __name__ == '__main__':
    app.run()
