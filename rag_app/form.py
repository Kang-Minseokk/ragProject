from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired


class UserMsgForm(FlaskForm):
    user_msg = TextAreaField('user_msg', validators=[DataRequired()])

