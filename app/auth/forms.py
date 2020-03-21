from flask_wtf import FlaskForm
from wtforms import BooleanField,StringField,PasswordField,SubmitField
from wtforms.validators import Length,Email,DataRequired

class LoginForm(FlaskForm):
	email = StringField('E-mail',validators=[DataRequired(message= u'邮箱不能为空'),
											Email(message= u'请输入有效的邮箱地址，比如：username@domain.com')])
	password = PasswordField('密码')
	submit = SubmitField('Submit')
	

class RegisterForm(FlaskForm):
	username = StringField('用户名',validators=[DataRequired(message= u'用户名不能为空'),Length(3,18)])
	email = StringField('E-mail',validators=[DataRequired(message= u'邮箱不能为空'),
											Email(message= u'请输入有效的邮箱地址，比如：username@domain.com')])
	password = PasswordField('密码')
	submit = SubmitField('Submit')



