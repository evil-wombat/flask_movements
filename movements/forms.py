from flask_wtf import FlaskForm
from wtforms import IntegerField, DateField, StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, Length 


class MovementForm (FlaskForm):
    fecha = DateField ('fecha', validators = [DataRequired()])
    concepto = StringField ('concepto', validators = [DataRequired()])
    cantidad= FloatField ('cantidad', validators= [DataRequired()])

    submit = SubmitField ('Aceptar')
