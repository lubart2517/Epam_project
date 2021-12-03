from flask import abort, flash, redirect, render_template, url_for, request
from flask_login import current_user, login_required
from flask_paginate import Pagination, get_page_parameter, get_page_args
from ..forms.model_forms import BookForm, BookFormAddAuthor, BookFormDeleteAuthor, AuthorForm
from ..forms.query_forms import BooksQueryForm
from library import app, db
from ..service.book_service import BookService
from ..service.author_service import AuthorService
from ..service.orders_service import OrderService


def check_admin():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.role:
        abort(403)

# Books Views


@app.route('/admin/books/', methods=['GET', 'POST'], endpoint='admin_books')
@login_required
def admin_books():
    """
    List all books
    """
    check_admin()
    form = BooksQueryForm()
    page, per_page, offset = get_page_args()
    books = BookService.get_books()
    if form.validate_on_submit():
        query_filter = request.form.get('filter')
        if query_filter:
            to_find = request.form.get('find')
            if to_find:
                books = BookService.filter(query_filter, to_find)
        query_sort = request.form.get('sort')
        books = BookService.sort(books, query_sort)
    else:
        books = BookService.get_books()
    i = (page - 1) * per_page
    books_for_render = books[i:i+per_page]
    pagination = Pagination(page=page, total=len(books), record_name='books', offset=offset)
    return render_template('admin/books.html',
                           books=books_for_render, pagination=pagination, form=form, title="Books")


@app.route('/admin/book/add', methods=['GET', 'POST'], endpoint='admin_add_book')
@login_required
def add_book():
    """
    Add a book to the database
    """
    check_admin()

    form = BookForm()
    if form.validate_on_submit():
        try:
            BookService.add_book(name=form.name.data,
                       description=form.description.data, count=form.count.data, author=form.author.data)
            flash('You have successfully added a new book.')
        except ValueError:
            # in case book name already exists
            flash('Error: book name already exists.')

        # redirect to books page
        return redirect(url_for('admin_books'))

    # load book template
    return render_template('admin/book_add.html', action="Add",
                           add_book=add_book, form=form,
                           title="Add Book")


@app.route('/admin/book/edit/<int:id>', methods=['GET', 'POST'], endpoint='admin_edit_book')
@login_required
def edit_book(id):
    """
    Edit a book with given id
    Admin can change bokk name, count, description and add or delte authors from book authors
     :param id: ID of the book
    """
    check_admin()

    book = BookService.get_book_by_id(id)
    form = BookForm(obj=book)
    del form.author
    add_author_form = BookFormAddAuthor(author_choices=BookService.get_free_authors(id))
    delete_author_form = BookFormDeleteAuthor(author_choices=BookService.get_authors(id))

    #  if admin adds author
    if add_author_form.validate_on_submit():
        BookService.add_author(id, add_author_form.author.data)
        flash('You have successfully added author to the book.')
        # redirect to the books page
        return redirect(url_for('admin_books'))

    #  if admin deletes author
    if delete_author_form.validate_on_submit():
        BookService.delete_author(id, delete_author_form.author.data)
        flash('You have successfully deleted author from the book.')
        # redirect to the books page
        return redirect(url_for('admin_books'))

    #  if admin changes book name, description or count
    if form.validate_on_submit():
        BookService.update(id, form.name.data, form.description.data, form.count.data)
        db.session.commit()
        flash('You have successfully edited the book.')

        # redirect to the books page
        return redirect(url_for('admin_books'))

    else:
        form.description.data = book.description
        form.name.data = book.name
        form.count.data = book.count
        add_author_form.author.data = BookService.get_free_authors(id)[0]
        delete_author_form.author.data = BookService.get_authors(id)[0]
        return render_template('admin/book_edit.html', action="Edit",
                               add_book=add_book, form=form,add_author_form=add_author_form,
                               book=book, title="Edit Book", delete_author_form=delete_author_form)


@app.route('/admin/book/delete/<int:id>', methods=['GET', 'POST'], endpoint='admin_delete_book')
@login_required
def delete_book(id):
    """
    Delete a book from the database
    :param id: ID of the book
    """
    check_admin()

    BookService.delete_book(id)
    flash('You have successfully deleted the book.')

    # redirect to the books page
    return redirect(url_for('admin_books'))


@app.route('/admin/authors/', methods=['GET', 'POST'], endpoint='admin_authors')
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


@app.route('/admin/author/add', methods=['GET', 'POST'], endpoint='admin_add_author')
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
        return redirect(url_for('admin_authors'))

    # load author template
    return render_template('admin/author.html', action="Add",
                           add=True, form=form)


@app.route('/admin/author/edit/<int:id>', methods=['GET', 'POST'], endpoint='admin_edit_author')
@login_required
def edit_author(id):
    """
    Edit author in the database
    """
    check_admin()
    author = AuthorService.get_author_by_id(id)
    form = AuthorForm(obj=author)
    if form.validate_on_submit():
        try:
            AuthorService.update(id=id, name=form.name.data,
                       middle_name=form.middle_name.data, last_name=form.last_name.data)
            flash('You have successfully edited author.')
        except ValueError:
            # in case author name already exists
            flash('Error: author name already exists.')

        # redirect to authors page
        return redirect(url_for('admin_authors'))

    # load author template
    return render_template('admin/author.html', action="Edit",
                           add=False, form=form)


@app.route('/admin/author/delete/<int:id>', methods=['GET', 'POST'], endpoint='admin_delete_author')
@login_required
def delete_author(id):
    """
    Delete a author from the database
    :param id: ID of the author
    """
    check_admin()

    AuthorService.delete_author(id)
    flash('You have successfully deleted the author.')

    # redirect to the books page
    return redirect(url_for('admin_authors'))


@app.route('/admin/orders/', methods=['GET', 'POST'], endpoint='admin_orders')
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


@app.route('/admin/order/close/<int:id>', methods=['GET', 'POST'], endpoint='admin_close_order')
@login_required
def close_order(id):
    """
    Delete a author from the database
    :param id: ID of the author
    """
    check_admin()

    OrderService.close_order(id)
    flash('You have successfully closed the order.')

    # redirect to the books page
    return redirect(url_for('admin_orders'))


@app.route('/admin/order/add', methods=['GET', 'POST'], endpoint='admin_add_order')
@login_required
def add_order():
    """
    Add an order to the database
    """
    check_admin()

    form = AuthorForm()
    if form.validate_on_submit():
        try:
            AuthorService.add_author(name=form.name.data,
                       middle_name=form.middle_name.data, last_name=form.last_name.data)
            flash('You have successfully added a new order.')
        except ValueError:
            # in case author name already exists
            flash('Error: author name already exists.')

        # redirect to authors page
        return redirect(url_for('admin_authors'))

    # load author template
    return render_template('admin/author.html', action="Add",
                           add=True, form=form)