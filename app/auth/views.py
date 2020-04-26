# encoding: utf-8
from flask_mako import render_template
from . import auth
from app.auth.forms import LoginForm,RegisterForm
from app.models import User,db
from flask_login import login_user,logout_user,login_required,current_user
from flask import redirect,url_for,flash
from flask_mako import render_template

@auth.route('/signup',methods=['GET','POST'])
def signup():
	form = RegisterForm()
	if form.validate_on_submit():
		user = User(email=form.email.data,
					username=form.username.data,
					password=form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('注册成功！', 'info')
		return redirect(url_for('auth.signin'))

	return render_template('/auth/signup.html',form=form)

@auth.route('/signin', methods=['GET','POST'])
def signin():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user is None:
			flash('用户不存在,需要在下方注册！','danger')
			return redirect(url_for('auth.signup'))
		elif user.verify_password(form.password.data):
			login_user(user)
			flash('登录成功', 'success')
			return redirect(url_for('user.index'))
		else:
			flash("密码错误！", 'danger')
			return redirect(url_for('auth.signin'))
	return render_template('/auth/signin.html',
							title='signin',
							form=form)

@auth.route('/signout')
@login_required
def signout():
	logout_user()
	flash('退出成功！', 'primary')
	return redirect(url_for('user.index'))

