from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms.fields.html5 import DateField
from app import create_app
import getpass 

class OrderForm(FlaskForm):
    """
    Form for users to ask authorized an order
    """
    tipo_tramite = SelectField('Tipo de tramite', choices=[
        ('Autorizaciones medicas: cirugias, estudios y practicas','Autorizaciones medicas: cirugias, estudios y practicas'),
        ('Autorizaciones odontologicas','Autorizaciones odontologicas'),
        ('Autorizaciones de Medicamentos de Tratamientos Especiales','Autorizaciones de Medicamentos de Tratamientos Especiales')],
        validators=[DataRequired()])
    observaciones = TextAreaField('Observaciones', validators=[DataRequired()])
    image = FileField('Documentacion requerida', validators=[DataRequired()])
    submit = SubmitField('Upload')

