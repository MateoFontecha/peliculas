from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.inventario import Inventarios
from app.models.pelicula import Peliculas 
from app import db

bp = Blueprint('inventario', __name__)
@bp.route('/inventario')
def index():
    data = Inventarios.query.all()
    pel = Peliculas.query.all()
   
    return render_template('inventarios/index.html', data=data,pel=pel)

@bp.route('/inventario/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        id_pelicula = request.form['id_pelicula']
        estado = request.form['estado']
        fecha_adquisicion = request.form['fecha_adquisicion']
        
        
        new_inventario = Inventarios(id_pelicula=id_pelicula, estado=estado, fecha_adquisicion=fecha_adquisicion)
        db.session.add(new_inventario)
        db.session.commit()
        
        return redirect(url_for('inventario.index'))
    pel = Peliculas.query.all()
    return render_template('inventarios/add.html',pel=pel)

@bp.route('/inventario/edit/<int:idInventario>', methods=['GET', 'POST'])
def edit(idInventario):
    inventario = Inventarios.query.get_or_404(idInventario)

    if request.method == 'POST':
        inventario.id_pelicula = request.form['id_pelicula']
        inventario.estado = request.form['estado']
        inventario.fecha_adquisicion = request.form['fecha_adquisicion']
        
        db.session.commit()
        return redirect(url_for('inventario.index'))

    return render_template('inventarios/edit.html', inventario=inventario)
    

@bp.route('/inventario/delete/<int:idInventario>')
def delete(idInventario):
    inventario = Inventarios.query.get_or_404(idInventario)
    
    db.session.delete(inventario)
    db.session.commit()

    return redirect(url_for('inventario.index'))