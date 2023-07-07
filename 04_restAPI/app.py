from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def basic():
    if request.method == 'POST':
        firstname = request.json['firstname']
        return jsonify ({
            'firstname' : firstname
        })
    return jsonify({
        'firstname' : 'asdf'
    })

# {
#     "key" : "element"
# }


if __name__ == '__main__':
    app.run(debug=True)