from app import db

class Cliente(db.Model):
    id_clientes = db.Column(db.Integer, primary_Key=True)
    nombre = db.COlumn(db.Strimg(255), nullable=False)
    apellido = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(255), nullable=False)
    direccion = db.Column(db.Strimg(255), nullable=False)