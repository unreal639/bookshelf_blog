from . import api
from flask import jsonify
from app.models import db, Book

@api.route('/books',methods=['GET'])
def query_books_api():
	books = Book.query.all()
	if books:
		books_dict = [{'bookid':book.bookid,
						'title':book.title,
						'body':book.body,
						'create_time':book.create_time}
						for book in books]
		return jsonify(books_dict)
	return jsonify({'status':'no datas'})


@api.route('/book/<int:bookid>',methods=['DELETE'])
def del_book_api(bookid):
	book = db.session.query(Book).filter(Book.bookid==bookid).first()
	if book:
		db.session.delete(book)
		db.session.commit()
		return jsonify({'status':'delete success <book id:{}>'.format(bookid)})
	return jsonify({'status':'can not find the book'})