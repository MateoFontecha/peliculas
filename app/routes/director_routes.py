from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.director import Directores
from app import db

bp = Blueprint('director', __name__)
@bp.route('/director')
def index():
    data = Directores.query.all()
   
    return render_template('directores/index.html', data=data)

@bp.route('/director/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
    
        new_director = Directores(nombre=nombre)
        db.session.add(new_director)
        db.session.commit()
        
        return redirect(url_for('director.index'))

    return render_template('directores/add.html')

@bp.route('/director/edit/<int:idDirector>', methods=['GET', 'POST'])
def edit(idDirector):
    director = Directores.query.get_or_404(idDirector)

    if request.method == 'POST':
        director.nombre = request.form['nombre']
   
        db.session.commit()
        return redirect(url_for('director.index'))

    return render_template('directores/edit.html', director=director)
    

@bp.route('/director/delete/<int:idDirector>')
def delete(idDirector):
    director = Directores.query.get_or_404(idDirector)
    
    db.session.delete(director)
    db.session.commit()

    return redirect(url_for('director.index'))