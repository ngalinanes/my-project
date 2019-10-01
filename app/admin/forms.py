from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo
from app import create_app
from ..models import Orden

class EditOrderForm(FlaskForm):
    """
    Form para editar el estado de una orden
    """
    nombre = StringField('Usuario del paciente')
    estado = SelectField('Estado', choices=[
        ('Pendiente','Pendiente'),
        ('Autorizada','Autorizada'),
        ('Rechazada','Rechazada')],
        validators=[DataRequired()])

    submit = SubmitField('Editar')
