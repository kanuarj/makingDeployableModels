from flask import Flask

app = Flask(__name__)

@app.route('/')
def basic():
    return 'Hello to all STTP listeners'

if __name__ == '__main__':
    app.run(debug=True)