from app import db

class Clientes(db.Model):

    __tablename__ = 'cliente'
    idCliente = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    apellido = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(255), nullable=False)
    direccion = db.Column(db.String(255), nullable=False)
    
    rentas = db.relationship('Rentas', back_populates = 'cliente')    

      
       
        
         
          
           
            
             






               