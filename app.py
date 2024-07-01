from flask import Flask,render_template,request,redirect,url_for
import os
from PIL import Image
import numpy as np
import tensorflow as tf


app = Flask(__name__)
app.config['Uploaded_data'] = './static/uploads/'

model = tf.keras.applications.ResNet50(weights='imagenet')

def preprocess_image(image_path):
    img = Image.open(image_path)
    resized = img.resize([224,224])
    img_arr = np.array(resized)
    exp_dim = np.expand_dims(img_arr,axis=0)
    return exp_dim

def predict(image_path):
    exp_dim = preprocess_image(image_path)
    predictions = model.predict(exp_dim)
    return tf.keras.applications.imagenet_utils.decode_predictions(predictions,top=1)[0]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict_image():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file_path = os.path.join(app.config['Uploaded_data'],file.filename)
            file.save(file_path)
            predictions = predict(file_path)
            return render_template('predict.html',predictions=predictions,image_file_name=file.filename)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)