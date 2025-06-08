from fastapi import APIRouter, UploadFile, File
from service.predict_service import predict_image_service

router = APIRouter()

@router.post("/predict", tags=["ML Model"])
async def predict_image(file: UploadFile = File(...)):
    """
    Endpoint to predict the class of an uploaded image.
    """
    image_bytes = await file.read()
    return predict_image_service(image_bytes)
