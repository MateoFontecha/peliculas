from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.genero import Generos
from app import db

bp = Blueprint('genero', __name__)
@bp.route('/genero')
def index():
    data = Generos.query.all()
   
    return render_template('generos/index.html', data=data)

@bp.route('/genero/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
     
        new_genero = Generos(nombre=nombre)
        db.session.add(new_genero)
        db.session.commit()
        
        return redirect(url_for('genero.index'))

    return render_template('generos/add.html')

@bp.route('/genero/edit/<int:idGenero>', methods=['GET', 'POST'])
def edit(idGenero):
    genero = Generos.query.get_or_404(idGenero)

    if request.method == 'POST':
        genero.nombre = request.form['nombre']

        db.session.commit()
        return redirect(url_for('genero.index'))

    return render_template('generos/edit.html', genero=genero)
    

@bp.route('/genero/delete/<int:idGenero>')
def delete(idGenero):
    genero = Generos.query.get_or_404(idGenero)
    
    db.session.delete(genero)
    db.session.commit()

    return redirect(url_for('genero.index'))