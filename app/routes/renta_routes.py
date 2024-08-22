from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.renta import Rentas
from app.models.cliente import Clientes
from app.models.empleado import Empleados
from app import db

bp = Blueprint('renta', __name__)

@bp.route('/')
def index():
    data = Rentas.query.all()
    
    
    return render_template('rentas/index.html', data=data)
  

@bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':

        fecha_renta = request.form['fecha_renta']
        fecha_devolucion = request.form['fecha_devolucion']
        total = request.form['total']
        cliente_id = request.form['cliente_id']
        empleado_id = request.form['empleado_id']
        
        new_renta = Rentas(fecha_renta=fecha_renta, fecha_devolucion=fecha_devolucion, total=total, cliente_id=cliente_id, empleado_id=empleado_id)
        db.session.add(new_renta)
        db.session.commit()
        
        return redirect(url_for('renta.index'))
    data = Clientes.query.all()
    emple = Empleados.query.all()
    return render_template('rentas/add.html', data=data, emple=emple)

@bp.route('/edit/<int:idRenta>', methods=['GET', 'POST'])
def edit(idRenta):
    renta = Rentas.query.get_or_404(idRenta)

    if request.method == 'POST':
        #return "entra al if"
        renta.fecha_renta = request.form['fecha_renta']
        renta.fecha_devolucion = request.form['fecha_devolucion']
        renta.total = request.form['total']
        renta.cliente_id = request.form['cliente_id']
        renta.empleado_id = request.form['empleado_id']
        
        db.session.commit()
        
        return redirect(url_for('renta.index'))

    return render_template('rentas/edit.html', renta=renta)

@bp.route('/delete/<int:idRenta>')
def delete(idRenta):
    renta = Rentas.query.get_or_404(idRenta)
    
    db.session.delete(renta)
    db.session.commit()

    return redirect(url_for('renta.index'))


