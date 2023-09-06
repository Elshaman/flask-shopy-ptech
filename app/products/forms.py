from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import InputRequired, NumberRange
from flask_wtf.file import FileField, FileRequired, FileAllowed

#Formulario de registro
#de nuevo producto
class NewProductForm(FlaskForm):
    nombre = StringField(validators= [ InputRequired(message="falta nombre") ],
                         label = "ingrese nombre:")
    precio = IntegerField(label = "ingrese precio:" ,
                          validators=[ 
                                        InputRequired(
                                            message = "precio requerido"
                                        ), 
                                        NumberRange(
                                            message = "precio fuera de rango",
                                            min = 1000, 
                                            max = 10000
                                        )
                                     ])
    imagen = FileField(label = "cargue imagen del producto:" , 
                       validators =[
                           FileRequired(
                               message="Suba una imagen"
                           ),
                           FileAllowed(
                               ["jpg" , "png"], 
                               message="tipo de archivo incorrecto"
                           )
                       ])
    submit = SubmitField ("Registrar")