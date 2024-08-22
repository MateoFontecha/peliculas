from app import db

class Generos (db.Model):
    __tablename__ = 'genero'
    idGenero = db.Column(db.Integer, primary_key= True)
    nombre = db.Column(db.String(255), nullable= False)
    
    peliculas = db.relationship('Peliculas', back_populates = 'generos')
