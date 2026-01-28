# 1. Imagen base: Una versión ligera de Python
FROM python:3.11-slim

# 2. Directorio de trabajo: Donde vivirá la app dentro del contenedor
WORKDIR /app

# 3. Copiar dependencias primero (para optimizar la caché de Docker)
COPY requirements.txt .

# 4. Instalar las librerías
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar TODO el código de mi carpeta al contenedor
COPY . .

# 6. Comando para arrancar la app (ya no usamos el del yaml)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]