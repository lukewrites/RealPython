from flask_wtf import Form
from wtforms import TextField, DateField, IntegerField, SelectField, PasswordField
from wtforms.validators import DataRequired


class AddTask(Form):
    task_id = IntegerField('Priority')
    name = TextField('Task Name', validators=[DataRequired()])
    due_date = DateField(
        'Due Date (mm/dd/yyyy)',
        validators=[DataRequired()], format='%m/%d/%Y'
    )
    priority = SelectField(
        'Priority',
        validators=[DataRequired()],
        choices=[
            ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'),
            ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')
        ]
    )
    status = IntegerField('Status')
    posted_date = DateField('Posted Date (mm/dd/yyyy', validators=[DataRequired()], format='%m/%d/%Y')
