from wtforms import Form,BooleanField,TextField,PasswordField,validators,SubmitField,RadioField
from wtforms.validators import DataRequired

class LoginFrom(Form):
    username = TextField('Username', [validators.Length(min=2, max=25)])
    password = PasswordField("password",[validators.Length(min=2, max=25)])
    submit =SubmitField("submit")

class TodolistFrom(Form):
    title = TextField("标题",[validators.Length(min=1, max=64)])
    status = RadioField("是否完成",validators=[DataRequired()],  choices=[("1", '是'),("0",'否')])
    submit =SubmitField("submit")
