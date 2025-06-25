# Usar imagen base de Python
FROM python:3.12-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app_denue

# Copia solo archivos necesarios para instalar dependencias
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Ahora copia el resto del código
COPY . .

# Expone el puerto 5000 para Flask
EXPOSE 5000

# Comando para iniciar Flask
CMD ["python", "app.py"]
