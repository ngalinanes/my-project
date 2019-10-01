# app/auth/forms.py

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError, SelectField
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import User


class RegistrationForm(FlaskForm):
    """
    Form for users to create new account
    """
    nro_afiliado = StringField('Numero de afiliado', validators=[DataRequired()])
    first_name = StringField('Nombre', validators=[DataRequired()])
    last_name = StringField('Apellido', validators=[DataRequired()])
    telefono = StringField('Telefono', validators=[DataRequired()])
    ciudad = StringField('Ciudad', validators=[DataRequired()])
    direccion = StringField('Direccion', validators=[DataRequired()])
    estado_civil = SelectField('Estado civil', choices=[
        ('Soltero','Soltero'),
        ('Casado','Casado'),
        ('Otro','Otro')],
        validators=[DataRequired()])
    email = StringField('Correo electronico', validators=[DataRequired(), Email()])
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contrasena', validators=[
                                        DataRequired(),
                                        EqualTo('confirm_password')
                                        ])
    confirm_password = PasswordField('Confirmar contrasena')
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Ese correo electronico ya esta en uso.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Ese nombre de usuario ya esta en uso.')


class LoginForm(FlaskForm):
    """
    Form for users to login
    """
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
