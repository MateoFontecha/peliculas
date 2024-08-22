from app import db

class Rentas (db.Model):

    __tablename__ = 'renta'

    idRenta = db.Column(db.Integer, primary_key=True)
    fecha_renta = db.Column(db.DATE, nullable=False)
    fecha_devolucion = db.Column(db.DATE, nullable=False)
    total = db.Column(db.String(255), nullable =False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.idCliente')) 
    empleado_id = db.Column(db.Integer, db.ForeignKey('empleado.idEmpleado')) 


    cliente = db.relationship('Clientes', back_populates = 'rentas')
    empleados = db.relationship('Empleados', back_populates ='rentas')
    detalles = db.relationship('DetallesRentas', back_populates = 'rentas')
        
