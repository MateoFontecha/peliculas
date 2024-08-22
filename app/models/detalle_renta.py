from app import db


class DetallesRentas(db.Model):
    __tablename__ = 'detalle_renta'
    inventario_id = db.Column(db.Integer, db.ForeignKey('inventario.idInventario'))
    renta_id = db.Column(db.Integer, db.ForeignKey('renta.idRenta'))
    idDetalleRenta = db.Column(db.Integer, primary_key =True)
    fecha_devolucion = db.Column(db.DATE, nullable = False)

    inventarios = db.relationship('Inventarios', back_populates='detalles')
    rentas = db.relationship('Rentas', back_populates='detalles')

