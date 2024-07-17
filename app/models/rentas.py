from app import db

class Rentas (db.Model):
    id_rentas = db.Column(db.Intenger, primary_Key=True)
    fecha_renta = db.column(db.DATE, nullable=False)
    fecha__devolucion = db.Column(db.DATE, nullable=False)
    total = db.Column(db.VARCHAR(255), nullable =False)
    idclientes = db.Column(db.Integer, db.ForeingnKey('clientes.id')) 
        
