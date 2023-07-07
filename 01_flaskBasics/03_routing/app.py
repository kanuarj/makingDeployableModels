from flask import Flask

app = Flask(__name__)

@app.route('/random')
def basic():
    return 'Hello World'

@app.route('/name/<name>')
def nameCaller(name):
    return f'Hello {name}'


if __name__ == '__main__':
    app.run(debug=True)