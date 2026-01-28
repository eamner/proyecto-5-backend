from fastapi import FastAPI, HTTPException
import psycopg2
import os

app = FastAPI()


# ********************************************************************************
# Función para obtener conexión a la DB
def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )


# Crear la tabla si no existe al iniciar la app
conn = get_db_connection()
cur = conn.cursor()
cur.execute(
    "CREATE TABLE IF NOT EXISTS tareas (id serial PRIMARY KEY, titulo varchar(100) NOT NULL);"
)
conn.commit()
cur.close()
conn.close()
# ********************************************************************************


@app.get("/")
def home():
    return {"status": "API Funcional", "endpoint": "/tareas (POST o GET)"}


# RUTA PARA GUARDAR UNA TAREA
@app.post("/tareas")
def crear_tarea(titulo: str):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO tareas (titulo) VALUES (%s) RETURNING id;", (titulo,))
        id_tarea = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return {"mensaje": "Tarea guardada", "id": id_tarea, "titulo": titulo}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# RUTA PARA VER TODAS LAS TAREAS
@app.get("/tareas")
def obtener_tareas():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tareas;")
    tareas = cur.fetchall()
    cur.close()
    conn.close()
    return {"tareas": tareas}
