from flask_wtf import FlaskForm
from wtforms import BooleanField,StringField,PasswordField,SubmitField
from wtforms.validators import Length,Email,DataRequired


class InfoForm(FlaskForm):
	about_me = StringField('信息')



class ChangePasswordForm(FlaskForm):
	old_password = PasswordField('旧密码')
	new_password = PasswordField('新密码')