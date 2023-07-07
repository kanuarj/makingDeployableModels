from flask import Flask, render_template, request, redirect, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from werkzeug.utils import secure_filename


model = load_model('./savedModels/model.h5')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def basic():
    if request.method == 'POST':
        path = request.files['filepath']
        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, 'testingImages', secure_filename(path.filename))
        path.save(file_path)

        input_image = image.load_img(file_path, color_mode='grayscale', target_size=(28, 28))
        numerical_values = image.img_to_array(input_image)
        expand_dimensions = np.expand_dims(numerical_values, axis=0)
        predicted_value = model.predict(expand_dimensions)
        argmax_pred = np.argmax(predicted_value)
        return render_template('response.html', digit=str(argmax_pred))
    return render_template('index.html')

@app.route('/redirects', methods=['POST'])
def redirects():
    if request.method == 'POST':
        return redirect(url_for('basic'))

if __name__ == '__main__':
    app.run(debug=True)