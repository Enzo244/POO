from __main__ import app
from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy(app)

class trabajador(db.Model):
    __tablaname__ = 'trabajador'

    id= db.Column(db.Integer, primary_key=True)
    nombre= db.Column(db.String(50), nullable=False)
    apellido= db.Column(db.String(50), nullable=False)
    dni= db.Column(db.String(10), nullable=False)
    correo=db.Column(db.String(100), nullable=False)
    legajo=db.Column(db.String(20), nullable=False)
    horas=db.Column(db.Integer, nullable=False)  # Horas semanales a cumplir
    funcion=db.Column(db.String(2), nullable=False)  # DO, AD, TE

    registros = db.relationship('RegistroHorario', backref='trabajador', cascade="all, delete-orphan")
