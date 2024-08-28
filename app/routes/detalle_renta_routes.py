from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.detalle_renta import DetallesRentas
from app.models.inventario import Inventarios
from app.models.renta import Rentas
from app import db

bp = Blueprint('detalle_renta', __name__)
@bp.route('/detalle_renta')
def index():
    data = DetallesRentas.query.all()
   
    return render_template('detalles_rentas/index.html', data=data)

@bp.route('/detalle_renta/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        fecha_devolucion = request.form['fecha_devolucion']
        renta_id = request.form['renta_id']
        inventario_id = request.form['inventario_id']
        
        
        new_detalle_renta = DetallesRentas(fecha_devolucion=fecha_devolucion, renta_id=renta_id, inventario_id=inventario_id)
        db.session.add(new_detalle_renta)
        db.session.commit()
        
        return redirect(url_for('detalle_renta.index'))
    ren = Rentas.query.all()
    inven = Inventarios.query.all()

    return render_template('detalles_rentas/add.html',ren=ren,inven=inven)

@bp.route('/detalle_renta/edit/<int:idDetalleRenta>', methods=['GET', 'POST'])
def edit(idDetalleRenta):
    detalle_renta = DetallesRentas.query.get_or_404(idDetalleRenta)

    if request.method == 'POST':
        detalle_renta.fecha_devolucion = request.form['fecha_devolucion']
        detalle_renta.renta_id = request.form['renta_id']
        detalle_renta.inventario_id = request.form['inventario_id']
        
        db.session.commit()
        return redirect(url_for('detalle_renta.index'))

    return render_template('detalles_rentas/edit.html', detalle_renta=detalle_renta)
    

@bp.route('/detalle_renta/delete/<int:idDetalleRenta>')
def delete(idDetalleRenta):
    detalle_renta = DetallesRentas.query.get_or_404(idDetalleRenta)
    
    db.session.delete(detalle_renta)
    db.session.commit()

    return redirect(url_for('detalle_renta.index'))