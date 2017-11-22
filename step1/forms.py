from wtforms import Form,BooleanField,TextField,PasswordField,validators,SubmitField

class LoginFrom(Form):
    username = TextField('Username', [validators.Length(min=2, max=25)])
    password = PasswordField("password",[validators.Length(min=2, max=25)])
    submit =SubmitField("submit")