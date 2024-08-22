from app import db 

class Peliculas (db.Model):
    
    __tablename__ = 'pelicula'
    idPelicula = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    año = db.Column(db.String(255), nullable=False)
    duracion = db.Column(db.String(255), nullable=False)
    id_genero = db.Column(db.Integer, db.ForeignKey('genero.idGenero'))
    id_director = db.Column(db.Integer,db.ForeignKey('director.idDirector'))
    id_empleado = db.Column(db.Integer,db.ForeignKey('empleado.idEmpleado'))
    
    generos = db.relationship('Generos', back_populates = 'peliculas')

    inventarios = db.relationship('Inventarios', back_populates = 'peliculas')
    directores = db.relationship('Directores', back_populates = 'peliculas')
    empleados = db.relationship('Empleados',back_populates = 'peliculas')
