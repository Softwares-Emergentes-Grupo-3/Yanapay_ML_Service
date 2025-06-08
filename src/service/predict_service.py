from ai_model.load_model import get_model
from ai_model.predict import predict_with_model
from dto.response.predict_response import PredictResponse

model = get_model()
#class_names = ['Early_blight', 'Healthy', 'Late_blight']
class_names = ['Tizon Temprano', 'Saludable', 'Tizon Tardio']

def predict_image_service(image_bytes: bytes) -> PredictResponse:
    prediction, confidence = predict_with_model(model, image_bytes, class_names)
    return PredictResponse(prediction=prediction, confidence=confidence)
