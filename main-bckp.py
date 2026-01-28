from fastapi import FastAPI
import psycopg2
import redis
import os

app = FastAPI()


@app.get("/")
def home():
    status = {
        "message": "Hola desde FastAPI!",
        "database": "Desconectada",
        "redis": "Desconectada",
    }
    # Probar PostgreSQL
    try:
        conn = psycopg2.connect(
            host="db",
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
        )
        status["database"] = "Conectada ✅"
        conn.close()
    except Exception as e:
        status["database"] = f"❌ Error de conexión: {e}"

    # Probar Redis
    try:
        pass_redis = os.getenv("REDIS_PASSWORD")
        r = redis.Redis(
            host="cache",
            port=6379,
            password=pass_redis,
        )
        if r.ping():
            status["redis"] = "Conectada ✅"
    except Exception as e:
        status["redis"] = f"❌ Error de conexión: {e}"
    return status
