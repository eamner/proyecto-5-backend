# 🚀 API de Gestión - Proyecto 5

Sistema de API REST desarrollado con **FastAPI**, utilizando **PostgreSQL** para persistencia de datos y **Redis** para optimización de caché, todo orquestado con **Docker**.

## 🌐 Demo en Vivo
Puedes probar la API desplegada en Render aquí: 
👉https://mi-primera-api-v2.onrender.com/docs 

## 🛠️ Stack Tecnológico
* **Lenguaje:** Python 3.x
* **Framework:** FastAPI
* **Base de Datos:** PostgreSQL
* **Caché:** Redis
* **Contenerización:** Docker & Docker Compose
* **Despliegue:** Render

## ⚙️ Configuración Local
Para correr este proyecto en tu máquina (Kubuntu u otro):

1. **Clonar el repo:**
   ```bash
   git clone [https://github.com/eamner/proyecto-5-backend.git](https://github.com/eamner/proyecto-5-backend.git)
Configurar variables: Copia el archivo .env.example a .env y rellena tus credenciales.

Levantar con Docker:

Bash

docker-compose up --build
📈 Características
Documentación automática con Swagger (Ruta /docs).

Conexión segura a base de datos mediante variables de entorno.

Arquitectura escalable lista para producción.

