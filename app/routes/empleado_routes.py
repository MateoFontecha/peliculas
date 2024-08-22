from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.empleado import Empleados
from app import db

bp = Blueprint('empleado', __name__)
@bp.route('/empleado')
def index():
    data = Empleados.query.all()
   
    return render_template('empleados/index.html', data=data)

@bp.route('/empleado/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = request.form['telefono']
        correo = request.form['correo']
        
        new_empleado = Empleados(nombre=nombre, apellido=apellido, telefono=telefono, correo=correo)
        db.session.add(new_empleado)
        db.session.commit()
        
        return redirect(url_for('empleado.index'))

    return render_template('empleados/add.html')

@bp.route('/empleado/edit/<int:idEmpleado>', methods=['GET', 'POST'])
def edit(idEmpleado):
    empleado = Empleados.query.get_or_404(idEmpleado)

    if request.method == 'POST':
        empleado.nombre = request.form['nombre']
        empleado.apellido = request.form['apellido']
        empleado.telefono = request.form['telefono']
        empleado.correo = request.form['correo']
        db.session.commit()
        return redirect(url_for('empleado.index'))

    return render_template('empleados/edit.html', empleado=empleado)
    

@bp.route('/Empleado/delete/<int:idEmpleado>')
def delete(idEmpleado):
    empleado = Empleados.query.get_or_404(idEmpleado)
    
    db.session.delete(empleado)
    db.session.commit()

    return redirect(url_for('empleado.index'))