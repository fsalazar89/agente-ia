# Usamos una imagen ligera de Python
FROM python:3.11-slim

# Evita que Python genere archivos .pyc y permite ver logs en tiempo real
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Copiamos el archivo de requerimientos
COPY requirements.txt .

# Instalamos las librerías directamente en el sistema del contenedor
# Usamos --no-cache-dir para que la imagen sea más pequeña
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del código
COPY . .

CMD ["python", "main.py"]