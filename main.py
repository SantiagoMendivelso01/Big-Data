from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import get_db

app = FastAPI(title="Sakila API")

@app.get("/")
def root():
    return {"message": "FastAPI conectado a Aurora Sakila ✅"}

@app.get("/actores")
def get_actores(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT actor_id, first_name, last_name FROM actor LIMIT 10"))
    return [{"id": r[0], "nombre": r[1], "apellido": r[2]} for r in result.fetchall()]

@app.get("/peliculas")
def get_peliculas(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT film_id, title, release_year, rental_rate FROM film LIMIT 10"))
    return [{"id": r[0], "titulo": r[1], "año": r[2], "precio": r[3]} for r in result.fetchall()]

@app.get("/clientes")
def get_clientes(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT customer_id, first_name, last_name, email FROM customer LIMIT 10"))
    return [{"id": r[0], "nombre": r[1], "apellido": r[2], "email": r[3]} for r in result.fetchall()]
