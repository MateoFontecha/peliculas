from app import db

class Directores(db.Model):
    __tablename__ = 'director'
    idDirector = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable =False)
    
    peliculas = db.relationship('Peliculas', back_populates = 'directores')

