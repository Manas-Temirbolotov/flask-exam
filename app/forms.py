from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, SelectField, \
    validators, ValidationError, DateField

from .models import Position, Employee


class PositionForm(FlaskForm):
    name = StringField(label='Название позиции', validators=[validators.DataRequired()])
    department = StringField(label='Название отдела', validators=[validators.DataRequired()])
    wage = IntegerField(label='Заработная плата', validators=[validators.DataRequired()])
    submit = SubmitField(label='Сохранить')




class EmployeeForm(FlaskForm):
    name = StringField(label='ФИО сотрудника', validators=[validators.DataRequired()])
    birth_date = DateField(label='Дата рождения', validators=[validators.DataRequired()])
    position_id = SelectField(label='Идентификационный номер', validators=[validators.DataRequired()])
    submit = SubmitField(label='Сохранить')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        result = []
        for position in Position.query.all():
            result.append((position.id, position.name))
        self.position_id.choices = result

def validate_rating(self, wage):
    if wage.data < 0:
        raise ValidationError('Заработная плата не может быть меньше нуля')