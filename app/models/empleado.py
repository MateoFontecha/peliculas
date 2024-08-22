from app import db

class Empleados (db.Model):
    
    __tablename__ = 'empleado'
    
    idEmpleado = db.Column(db.Integer, primary_key =True)
    nombre = db.Column(db.String(255), nullable = False)
    apellido = db.Column(db.String(255), nullable =False)
    telefono = db.Column(db.Integer, nullable =False)
    correo = db.Column(db.String(255), nullable =False)

    rentas = db.relationship('Rentas', back_populates ='empleados' )
    peliculas = db.relationship('Peliculas', back_populates ='empleados')