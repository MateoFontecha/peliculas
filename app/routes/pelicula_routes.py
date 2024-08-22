from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.pelicula import Peliculas
from app.models.empleado import Empleados
from app.models.genero import Generos
from app.models.director import Directores
from app import db

bp = Blueprint('pelicula', __name__)
@bp.route('/pelicula')
def index():
    data = Peliculas.query.all()
    gen = Generos.query.all()
    em = Empleados.query.all()
    direc = Directores.query.all()
   
    return render_template('peliculas/index.html', data=data, em=em,gen= gen,direc=direc)

@bp.route('/pelicula/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        titulo = request.form['titulo']
        año = request.form['año']
        duracion = request.form['duracion']
        id_genero = request.form['id_genero']
        id_director = request.form['id_director']
        id_empleado = request.form['id_empleado']
        
        new_pelicula = Peliculas(titulo=titulo, año=año, duracion=duracion, id_genero=id_genero,id_director=id_director,id_empleado=id_empleado)
        db.session.add(new_pelicula)
        db.session.commit()
        
        return redirect(url_for('pelicula.index'))
    gen = Generos.query.all()
    em = Empleados.query.all()
    direc = Directores.query.all()

    return render_template('peliculas/add.html',gen=gen,em=em,direc=direc)

@bp.route('/pelicula/edit/<int:idPelicula>', methods=['GET', 'POST'])
def edit(idPelicula):
    pelicula = Peliculas.query.get_or_404(idPelicula)

    if request.method == 'POST':
        pelicula.titulo = request.form['titulo']
        pelicula.año = request.form['año']
        pelicula.duracion = request.form['duracion']
        pelicula.id_genero = request.form['id_genero']
        pelicula.id_director = request.form['id_director']
        pelicula.id_empleado = request.form['id_empleado']
        db.session.commit()
        return redirect(url_for('pelicula.index'))

    return render_template('peliculas/edit.html', pelicula=pelicula)
    

@bp.route('/pelicula/delete/<int:idPelicula>')
def delete(idPelicula):
    pelicula = Peliculas.query.get_or_404(idPelicula)
    
    db.session.delete(pelicula)
    db.session.commit()

    return redirect(url_for('pelicula.index'))
