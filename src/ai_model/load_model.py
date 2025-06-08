from tensorflow.keras.models import load_model
import os

def get_model():
    model_path = os.path.join(os.path.dirname(__file__), 'model.h5')
    return load_model(model_path)