# Imagen base de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar requerimientos e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código de la aplicación
COPY ./src/ .

# Exponer el puerto de la aplicación
EXPOSE 8000

# Comando para arrancar FASTAPI usando uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0", "--port", "8000"]