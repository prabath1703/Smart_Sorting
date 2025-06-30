from flask import Flask, render_template, request, url_for
from tensorflow.keras.preprocessing.image import load_img
import numpy as np
import tensorflow as tf
import os

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = tf.keras.models.load_model('healthy_vs_rotten.h5')

# Define class labels
classes = [
    'Apple__Healthy (0)', 'Apple__Rotten (1)', 'Banana__Healthy (2)', 'Banana__Rotten (3)',
    'Bellpepper__Healthy (4)', 'Bellpepper__Rotten (5)', 'Carrot__Healthy (6)', 'Carrot__Rotten (7)',
    'Cucumber__Healthy (8)', 'Cucumber__Rotten (9)', 'Grape__Healthy (10)', 'Grape__Rotten (11)',
    'Guava__Healthy (12)', 'Guava__Rotten (13)', 'Jujube__Healthy (14)', 'Jujube__Rotten (15)',
    'Mango__Healthy (16)', 'Mango__Rotten (17)', 'Orange__Healthy (18)', 'Orange__Rotten (19)',
    'Pomegranate__Healthy (20)', 'Pomegranate__Rotten (21)', 'Potato__Healthy (22)',
    'Potato__Rotten (23)', 'Strawberry__Healthy (24)', 'Strawberry__Rotten (25)',
    'Tomato__Healthy (26)', 'Tomato__Rotten (27)'
]

# Home page
@app.route('/')
def index():
    return render_template("index.html")

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    if 'pc_image' not in request.files:
        return "No file part in the request", 400

    file = request.files['pc_image']

    if file.filename == '':
        return "No file selected", 400

    # Save image to static/uploads
    upload_folder = 'static/uploads'
    os.makedirs(upload_folder, exist_ok=True)
    img_path = os.path.join(upload_folder, file.filename)
    file.save(img_path)

    # Preprocess the image
    img = load_img(img_path, target_size=(224, 224))
    image_array = np.array(img)
    image_array = np.expand_dims(image_array, axis=0)
    image_array = image_array / 255.0  # <-- ADD THIS

    # Predict
    pred = np.argmax(model.predict(image_array), axis=1)
    prediction = classes[int(pred)]
    print("Prediction:", prediction)

    return render_template("portfolio-details.html", predict=prediction)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=2222)
