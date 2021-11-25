from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from ..forms.model_forms import BookForm, BookFormAddAuthor
from library import app, db
from ..models.book_models import Book
from ..service.book_service import BookService
from ..service.author_service import AuthorService

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

    books = BookService.get_books()

    return render_template('admin/books.html',
                           books=books, title="Books")


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
    Edit a book
    """
    check_admin()

    book = BookService.get_book_by_id(id)
    form = BookForm(obj=book)
    del form.author
    add_author_form = BookFormAddAuthor(author_choices=BookService.get_free_authors(id))

    if add_author_form.validate_on_submit():
        BookService.add_author(id, add_author_form.author.data)
        flash('You have successfully added author to the book.')
        # redirect to the departments page
        return redirect(url_for('admin_books'))
    if form.validate_on_submit():
        book.name = form.name.data
        book.description = form.description.data
        book.count = form.count.data
        db.session.commit()
        flash('You have successfully edited the book.')

        # redirect to the departments page
        return redirect(url_for('admin_books'))

    else:
        form.description.data = book.description
        form.name.data = book.name
        form.count.data = book.count
        add_author_form.author.data = AuthorService.get_first()
        return render_template('admin/book_edit.html', action="Edit",
                               add_book=add_book, form=form,add_author_form=add_author_form,
                               book=book, title="Edit Book")


@app.route('/admin/book/delete/<int:id>', methods=['GET', 'POST'], endpoint='admin_delete_book')
@login_required
def delete_book(id):
    """
    Delete a book from the database
    """
    check_admin()

    BookService.delete_book(id)
    flash('You have successfully deleted the book.')

    # redirect to the books page
    return redirect(url_for('admin_books'))