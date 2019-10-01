# app/models.py

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
from app import db, login_manager


class User(UserMixin, db.Model):
    """
    Users table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'afiliados'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    ordenes = db.relationship('Orden', backref='afiliados',cascade = 'all, delete-orphan', lazy = 'dynamic')
    nro_afiliado = db.Column(db.Integer, index=True, unique=True)
    is_admin = db.Column(db.Boolean, default=False)
    telefono = db.Column(db.String(60), index=True)
    ciudad = db.Column(db.String(60), index=True)
    estado_civil = db.Column(db.String(60), index=True)
    direccion = db.Column(db.String(60), index=True)
    

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Orden(db.Model):

    __tablename__ = 'ordenes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    data = db.Column(db.LargeBinary)
    estado = db.Column(db.String(300), default='Pendiente')
    tipo = db.Column(db.String(300))
    observaciones = db.Column(db.String(300))
    afiliado = db.Column(db.String(60), db.ForeignKey('afiliados.username'), nullable = False)
    fecha = db.Column(db.DateTime, default=datetime.datetime.utcnow)