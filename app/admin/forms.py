from flask_wtf import FlaskForm
from wtforms import BooleanField,StringField,PasswordField,SubmitField,TextAreaField,FileField
from wtforms.validators import Length,Email,DataRequired
from flask_wtf.file import FileRequired, FileAllowed

class AddbookForm(FlaskForm):
	title = StringField('标题')
	body = TextAreaField('内容')
	image = FileField(validators=[
					FileRequired(),
					FileAllowed(['png', 'jpg', 'jpeg'])])
