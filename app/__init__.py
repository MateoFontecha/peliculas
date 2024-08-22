from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)


    from app.routes import genero_routes, cliente_routes, renta_routes, director_routes, empleado_routes, detalle_renta_routes,  inventario_routes, pelicula_routes
    app.register_blueprint(genero_routes.bp)
    app.register_blueprint(cliente_routes.bp)
    app.register_blueprint(director_routes.bp)
    app.register_blueprint(empleado_routes.bp)
    app.register_blueprint(pelicula_routes.bp)
    app.register_blueprint(inventario_routes.bp)
    app.register_blueprint(renta_routes.bp)
    app.register_blueprint(detalle_renta_routes.bp)

    return app