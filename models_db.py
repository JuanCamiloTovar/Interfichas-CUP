from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# TABLA DE EQUIPOS DE LAS INTERFICHAS

class Equipos(db.Model):
    __tablename__ = 'lista_equipos'
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    ficha = db.Column(db.Integer, nullable=False)
    equipo = db.Column(db.String(25), nullable=False)
    jornada = db.Column(db.String(6), nullable=False)

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    username = db.Column(db.String(25), nullable = False, unique=True)
    password = db.Column(db.String(40), nullable = False)