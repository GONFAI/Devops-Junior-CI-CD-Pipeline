FROM python:3.10-slim

WORKDIR /app

# Copiar dependencias primero (cache)
COPY app/requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

# Copiar aplicación y tests
COPY app app
COPY tests tests

# Ejecutar tests durante el build
RUN pytest

# Exponer puerto
EXPOSE 5000

# Comando de arranque
CMD ["python", "app/app.py"]
