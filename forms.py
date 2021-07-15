from flask_mail import Message
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms import validators
from wtforms.validators import DataRequired, Email
from wtforms.widgets import TextArea
from wtforms.fields.html5 import EmailField

class envioCorreos(Form):
    nombre = StringField('Nombre Completo', 
        [validators.Required(message = 'El nombre es un campo necesario.'),
        validators.Length(min=3, max=120, message='Ingrese un nombre valido.')])
    correo = EmailField('Correo Electronico', validators=[DataRequired('El correo electronico es obligatorio'), Email('Ingrese un corre valido')])
    comentario = StringField('Comentarios', widget=TextArea(), validators=[DataRequired('Agrega tus comentarios')])
    enviar = SubmitField('Enviar')