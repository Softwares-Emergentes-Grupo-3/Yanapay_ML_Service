#Importar FastAPI
from fastapi import FastAPI
from config.settings import settings
from controller import predict_controller

# Crear la aplicación FastAPI
app = FastAPI(
    title=settings.app_name,
    description=settings.app_description,
    version=settings.app_version,
)

# Importamos el controlador de predicción
app.include_router(predict_controller.router)

@app.get("/", tags=["Root"])
def root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.host, port=settings.port)