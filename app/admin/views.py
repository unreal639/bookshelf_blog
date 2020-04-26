# encoding: utf-8
from . import admin
from flask_mako import render_template
from app.admin.forms import AddbookForm
from app.models import Book, User, db
from flask import redirect,url_for,flash,request,current_app,request

@admin.route('/admin')
def admin_index():
	return render_template('/admin/admin.html')

@admin.route('/admin/bookinfo')
def bookinfo():
	books = Book.query.all()
	return render_template('/admin/bookinfo.html',books=books)


@admin.route('/admin/userinfo')
def userinfo():
	users = User.query.all()
	return render_template('/admin/userinfo.html',users=users)

@admin.route('/admin/add_book',methods=['GET','POST'])
def add_book():
	form = AddbookForm()
	if request.method == 'POST':
	#if form.validate_on_submit():
		title = form.title.data
		body = form.body.data
		image = request.files['image']
		path = current_app.config['IMAGES_PATH']
		image_name = image.filename
		image_path = path + image_name
		image.save(image_path)
		
		print(title,body,image_name)
		book = Book(title=title,body=body,cover_path=image_name)
		db.session.add(book)
		db.session.commit()
		print('success added')
		flash('添加成功！', 'success')
		return redirect(url_for('admin.bookinfo'))
	return render_template('/admin/add_book.html',form=form)

@admin.route('/admin/del_book/<int:book_id>')
def del_book(book_id):
	book = db.session.query(Book).filter(Book.bookid==book_id).first()
	db.session.delete(book)
	db.session.commit()
	flash('删除成功!', 'danger')
	return redirect(url_for('admin.bookinfo'))


@admin.route('/admin/edit_book/<int:book_id>',methods=['GET','POST'])
def edit_book(book_id):
	form = AddbookForm()
	book = db.session.query(Book).filter(Book.bookid==book_id).first()
	if request.method == 'POST':
		book.title = request.form['title']
		book.body = request.form['body']
		db.session.commit()
		flash('编辑成功!', 'warning')
		return redirect(url_for('admin.bookinfo'))
	return render_template('/admin/edit_book.html',book=book,form=form)


