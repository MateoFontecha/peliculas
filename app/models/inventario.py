from app import db

class Inventarios (db.Model):
    __tablename__ = 'inventario'
    idInventario = db.Column(db.Integer, primary_key= True)
    id_pelicula = db.Column(db.Integer, db.ForeignKey('pelicula.idPelicula'))
    estado = db.Column(db.String(255), nullable = False)
    fecha_adquisicion = db.Column(db.DATE, nullable= False)

    detalles = db.relationship('DetallesRentas', back_populates = 'inventarios')
    peliculas = db.relationship('Peliculas', back_populates = 'inventarios')
