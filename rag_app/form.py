from flask_wtf import FlaskForm
from wtforms import StringField


class UserinputForm(FlaskForm):
    content = StringField('user_input')
