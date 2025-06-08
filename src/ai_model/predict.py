import numpy as np
from PIL import Image
from io import BytesIO
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

def preprocess_image(image_bytes, target_size=(224, 224)):
    imag = Image.open(BytesIO(image_bytes)).convert("RGB")
    imag = imag.resize(target_size)
    img_array = image.img_to_array(imag)
    img_array = preprocess_input(img_array)
    return np.expand_dims(img_array, axis=0)

def predict_with_model(model, image_bytes, class_names):
    processed = preprocess_image(image_bytes)
    pred = model.predict(processed)
    index = int(np.argmax(pred))
    confidence = round(float(np.max(pred)) * 100, 2)
    return class_names[index], confidence