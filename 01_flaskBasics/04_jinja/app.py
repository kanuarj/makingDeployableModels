from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def basic():
    firstname = 'Raunak'
    return render_template('index.html', name=firstname)


if __name__ == '__main__':
    app.run(debug=True)