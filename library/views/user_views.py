from flask import render_template, request, redirect, url_for, jsonify, session
from flask_login import login_required, current_user
from flask_paginate import Pagination, get_page_args
from ..forms.query_forms import BooksQueryForm
from ..rest.books_rest_service import BookRestService
from ..service.author_service import AuthorService
from ..service.orders_service import OrderService
from .blueprint import user

# Books Views


@user.route('/user/books/', methods=['GET', 'POST'], endpoint='books')
@login_required
def user_books():
    """
    List all books and sort & filter if necessary
    """
    form = BooksQueryForm(sort=session['sort'], filter=session['filter'], find=session['to_find'])
    page, per_page, offset = get_page_args()
    books = BookRestService.get_books()
    if form.validate_on_submit():
        session['filter'] = request.form.get('filter')
        session['sort'] = request.form.get('sort')
        session['to_find'] = request.form.get('find')
        return redirect(url_for('user.books'))
    to_find = session['to_find']
    if to_find:
        books = BookRestService.filter(books, session['filter'], to_find)
    query_sort = session['sort']
    books = BookRestService.sort(books, query_sort)
    index = (page - 1) * per_page
    books_for_render = books.iloc[index:index+per_page]
    pagination = Pagination(page=page, total=len(books), record_name='books', offset=offset)
    return render_template('user/books.html',
                           books=books_for_render.itertuples(), pagination=pagination, form=form, title="Books")


@user.route('/user/authors/', methods=['GET', 'POST'], endpoint='authors')
@login_required
def user_authors():
    """
    List all authors
    """
    page, per_page, offset = get_page_args()
    authors = AuthorService.get_authors()
    i = (page - 1) * per_page
    authors_for_render = authors[i:i+per_page]
    pagination = Pagination(page=page, total=len(authors), record_name='authors', offset=offset)
    return render_template('user/authors.html',
                           authors=authors_for_render, pagination=pagination, title="Authors")


@user.route('/user/orders/', methods=['GET'], endpoint='orders')
@login_required
def user_orders():
    """
    List all orders of the user
    """
    page, per_page, offset = get_page_args()
    orders = OrderService.get_orders_by_user(current_user.id)
    i = (page - 1) * per_page
    orders_for_render = orders[i:i+per_page]
    pagination = Pagination(page=page, total=len(orders), record_name='orders', offset=offset)
    return render_template('user/orders.html',
                           orders=orders_for_render, pagination=pagination, title="Orders")


@user.route('/user/book/order/<int:book_id>', methods=['GET'], endpoint='order_book')
@login_required
def user_order_book(book_id):
    """
    Order book by some user
    """
    OrderService.add_order(current_user.id, book_id)
    return redirect(url_for('user.orders'))
