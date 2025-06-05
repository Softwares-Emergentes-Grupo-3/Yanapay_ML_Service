#Importar FastAPI
from fastapi import FastAPI
from config.settings import settings

#Crear la aplicación FastAPI
app = FastAPI(
    title=settings.app_name,
    description=settings.app_description,
    version=settings.app_version,
)

@app.get("/", tags=["Root"])
def root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.host, port=settings.port)