# pylint: disable=no-else-return
"""This module manage all views with admin access"""
from flask import abort, flash, redirect, render_template, url_for, request, session
from flask_login import current_user, login_required
from flask_paginate import Pagination, get_page_args
from library import db
from ..forms.model_forms import BookForm, BookFormAddAuthor, BookFormDeleteAuthor, AuthorForm
from ..forms.query_forms import BooksQueryForm
from ..service.book_service import BookService
from ..service.author_service import AuthorService
from ..service.orders_service import OrderService
from .blueprint import admin


def check_admin():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.role:
        abort(403)

# Books Views


@admin.route('/dashboard/', endpoint='dashboard')
@login_required
def admin_dashboard():
    """ admin start page"""
    # prevent non-admins from accessing the page
    check_admin()

    return render_template('home/admin_dashboard.html', title="Dashboard")


@admin.route('/admin/books/', methods=['GET', 'POST'], endpoint='books')
@login_required
def admin_books():
    """
    List all books and sort & filter if necessary
    """
    check_admin()
    form = BooksQueryForm()
    page, per_page, offset = get_page_args()
    books = BookService.get_books()
    if form.validate_on_submit():
        session['filter'] = request.form.get('filter')
        session['sort'] = request.form.get('sort')
        session['to_find'] = request.form.get('find')
        return redirect(url_for('admin.books'))
    to_find = session['to_find']
    if to_find:
        books = BookService.filter(session['filter'], to_find)
    query_sort = session['sort']
    books = BookService.sort(books, query_sort)
    i = (page - 1) * per_page
    books_for_render = books[i:i+per_page]
    pagination = Pagination(page=page, total=len(books), record_name='books', offset=offset)
    return render_template('admin/books.html',
                           books=books_for_render, pagination=pagination, form=form, title="Books")


@admin.route('/admin/book/add', methods=['GET', 'POST'], endpoint='add_book')
@login_required
def add_book():
    """
    Add a book to the database
    """
    check_admin()

    form = BookForm(author_choices=AuthorService.get_authors())
    if form.validate_on_submit():
        try:
            BookService.add_book(name=form.name.data,
            description=form.description.data, count=form.count.data, author=form.author.data)
            flash('You have successfully added a new book.')
        except ValueError:
            # in case book name already exists
            flash('Error: book name already exists.')

        # redirect to books page
        return redirect(url_for('admin.books'))

    # load book template
    return render_template('admin/book_add.html', action="Add",
                           add_book=add_book, form=form,
                           title="Add Book")


@admin.route('/admin/book/edit/<int:book_id>', methods=['GET', 'POST'], endpoint='edit_book')
@login_required
def edit_book(book_id):
    """
    Edit a book with given book_id
    Admin can change book name, count, description and add or delete authors from book authors
     :param book_id: book_id of the book
    """
    check_admin()

    book = BookService.get_book_by_id(book_id)
    form = BookForm(obj=book)
    del form.author
    add_author_form = BookFormAddAuthor(author_choices=BookService.get_free_authors(book_id))
    delete_author_form = BookFormDeleteAuthor(author_choices=BookService.get_authors(book_id))

    #  if admin adds author
    if add_author_form.validate_on_submit():
        BookService.add_author(book_id, add_author_form.author.data)
        flash('You have successfully added author to the book.')
        # redirect to the books page
        return redirect(url_for('admin.books'))

    #  if admin deletes author
    if delete_author_form.validate_on_submit():
        BookService.delete_author(book_id, delete_author_form.author.data)
        flash('You have successfully deleted author from the book.')
        # redirect to the books page
        return redirect(url_for('admin.books'))

    #  if admin changes book name, description or count
    if form.validate_on_submit():
        BookService.update(book_id, form.name.data, form.description.data, form.count.data)
        db.session.commit()
        flash('You have successfully edited the book.')

        # redirect to the books page
        return redirect(url_for('admin.books'))

    else:
        form.description.data = book.description
        form.name.data = book.name
        form.count.data = book.count
        add_author_form.author.data = BookService.get_free_authors(book_id)[0]
        delete_author_form.author.data = BookService.get_authors(book_id)[0]
        return render_template('admin/book_edit.html', action="Edit",
                               add_book=add_book, form=form,add_author_form=add_author_form,
                               book=book, title="Edit Book", delete_author_form=delete_author_form)


@admin.route('/admin/book/delete/<int:book_id>', methods=['GET', 'POST'], endpoint='delete_book')
@login_required
def delete_book(book_id):
    """
    Delete a book from the database
    :param book_id: ID of the book
    """
    check_admin()

    BookService.delete_book(book_id)
    flash('You have successfully deleted the book.')

    # redirect to the books page
    return redirect(url_for('admin.books'))


@admin.route('/admin/authors/', methods=['GET', 'POST'], endpoint='authors')
@login_required
def admin_authors():
    """
    List all authors
    """
    check_admin()
    page, per_page, offset = get_page_args()
    authors = AuthorService.get_authors()
    i = (page - 1) * per_page
    authors_for_render = authors[i:i+per_page]
    pagination = Pagination(page=page, total=len(authors), record_name='authors', offset=offset)
    return render_template('admin/authors.html',
                           authors=authors_for_render, pagination=pagination, title="Authors")


@admin.route('/admin/author/add', methods=['GET', 'POST'], endpoint='add_author')
@login_required
def add_author():
    """
    Add a author to the database
    """
    check_admin()

    form = AuthorForm()
    if form.validate_on_submit():
        try:
            AuthorService.add_author(name=form.name.data,
                       middle_name=form.middle_name.data, last_name=form.last_name.data)
            flash('You have successfully added a new author.')
        except ValueError:
            # in case author name already exists
            flash('Error: author name already exists.')

        # redirect to authors page
        return redirect(url_for('admin.authors'))

    # load author template
    return render_template('admin/author.html', action="Add",
                           add=True, form=form)


@admin.route('/admin/author/edit/<int:author_id>', methods=['GET', 'POST'], endpoint='edit_author')
@login_required
def edit_author(author_id):
    """
    Edit author in the database
    """
    check_admin()
    author = AuthorService.get_author_by_id(author_id)
    form = AuthorForm(obj=author)
    if form.validate_on_submit():
        try:
            AuthorService.update(author_id=author_id, name=form.name.data,
                       middle_name=form.middle_name.data, last_name=form.last_name.data)
            flash('You have successfully edited author.')
        except ValueError:
            # in case author name already exists
            flash('Error: author name already exists.')

        # redirect to authors page
        return redirect(url_for('admin.authors'))

    # load author template
    return render_template('admin/author.html', action="Edit",
                           add=False, form=form)


@admin.route('/admin/author/delete/<int:author_id>', methods=['GET', 'POST'], endpoint='delete_author')
@login_required
def delete_author(author_id):
    """
    Delete a author from the database
    :param author_id: ID of the author
    """
    check_admin()

    AuthorService.delete_author(author_id)
    flash('You have successfully deleted the author.')

    # redirect to the books page
    return redirect(url_for('admin.authors'))


@admin.route('/admin/orders/', methods=['GET', 'POST'], endpoint='orders')
@login_required
def admin_orders():
    """
    List all orders
    """
    check_admin()
    page, per_page, offset = get_page_args()
    orders = OrderService.get_orders()
    i = (page - 1) * per_page
    orders_for_render = orders[i:i+per_page]
    pagination = Pagination(page=page, total=len(orders), record_name='orders', offset=offset)
    return render_template('admin/orders.html',
                           orders=orders_for_render, pagination=pagination, title="Orders")


@admin.route('/admin/order/close/<int:order_id>', methods=['GET', 'POST'], endpoint='close_order')
@login_required
def close_order(order_id):
    """
    Close order with this id
    :param order_id: ID of the order
    """
    check_admin()

    OrderService.close_order(order_id)
    flash('You have successfully closed the order.')

    # redirect to the books page
    return redirect(url_for('admin.orders'))
