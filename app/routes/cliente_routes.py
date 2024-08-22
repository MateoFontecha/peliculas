from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.cliente import Clientes
from app import db

bp = Blueprint('cliente', __name__)
@bp.route('/cliente')
def index():
    data = Clientes.query.all()
   
    return render_template('clientes/index.html', data=data)

@bp.route('/cliente/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        
        new_cliente = Clientes(nombre=nombre, apellido=apellido, telefono=telefono, direccion=direccion )
        db.session.add(new_cliente)
        db.session.commit()
        
        return redirect(url_for('cliente.index'))

    return render_template('clientes/add.html')

@bp.route('/cliente/edit/<int:idCliente>', methods=['GET', 'POST'])
def edit(idCliente):
    cliente = Clientes.query.get_or_404(idCliente)

    if request.method == 'POST':
        cliente.nombre = request.form['nombre']
        cliente.apellido = request.form['apellido']
        cliente.telefono = request.form['telefono']
        cliente.direccion = request.form['direccion']
        db.session.commit()
        return redirect(url_for('cliente.index'))

    return render_template('clientes/edit.html', cliente=cliente)
    

@bp.route('/Cliente/delete/<int:idCliente>')
def delete(idCliente):
    cliente = Clientes.query.get_or_404(idCliente)
    
    db.session.delete(cliente)
    db.session.commit()

    return redirect(url_for('cliente.index'))