from . import user
from mako.template import Template
from flask_mako import render_template
from .forms import ChangePasswordForm 
from flask_login import current_user,login_required
from app.models import Book,db
from app import cache
from flask import request, redirect, url_for, flash

@user.route('/')
@user.route('/index')
#@cache.cached(timeout=60*60*6,query_string=True)
def index():
	#books = Book.query.all()
	page = request.args.get('page',1,type=int)
	pagination = Book.query.order_by(Book.bookid).paginate(page,per_page=6,error_out=False)
	books = pagination.items
	return render_template('/user/index.html',books=books,pagination=pagination)

@user.route('/book/<int:bookid>')
def book(bookid):
	book = db.session.query(Book).filter(Book.bookid==bookid).first()
	return render_template('user/book.html',book=book)

@user.route('/search')
def search():
	q = request.args.get('q', '')
	if q == '':
		flash('输入要搜索的关键字…', 'warning')
		return redirect(url_for('user.index'))
	elif len(q) < 3:
		flash('至少输入3个字符！','warning')
		return redirect(url_for('user.index'))
	page = request.args.get('page', 1, type=int)
	pagination = Book.query.whooshee_search(q).paginate(page, per_page=6)
	search_books = pagination.items
	print(search_books)
	return render_template('/user/search.html', books=search_books, pagination=pagination, q=q)



@user.route('/user/<int:uid>')
@login_required
def user(uid):

	return render_template('/user/user.html')


# @user.route('/user/<int:uid>/setting',method=['GET','POST'])
# def changepassword(uid):
# 	form = ChangePasswordForm()

# 	return render_template('/user/setting.html',form=form)

