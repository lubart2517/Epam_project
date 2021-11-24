from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from ..forms.model_forms import BookForm
from library import app, db
from ..models.book_models import Book


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

    books = Book.query.all()

    return render_template('admin/books.html',
                           books=books, title="Books")


@app.route('/admin/book/add', methods=['GET', 'POST'], endpoint='admin_add_book')
@login_required
def add_book():
    """
    Add a book to the database
    """
    check_admin()

    add_book = True

    form = BookForm()
    if form.validate_on_submit():
        book = Book(name=form.name.data,
                                description=form.description.data, count=form.count.data, authors=form.count.data)
        try:
            # add book to the database
            db.session.add(book)
            db.session.commit()
            flash('You have successfully added a new book.')
        except:
            # in case book name already exists
            flash('Error: book name already exists.')

        # redirect to books page
        return redirect(url_for('admin_books'))

    # load book template
    return render_template('admin/book.html', action="Add",
                           add_book=add_book, form=form,
                           title="Add Book")

@app.route('/admin/book/edit/<int:id>', methods=['GET', 'POST'], endpoint='admin_edit_book')
@login_required
def edit_book(id):
    """
    Edit a department
    """
    check_admin()

    add_book = False

    book = Book.query.get_or_404(id)
    form = BookForm(obj=book)
    if form.validate_on_submit():
        book.name = form.name.data
        book.description = form.description.data
        db.session.commit()
        flash('You have successfully edited the book.')

        # redirect to the departments page
        return redirect(url_for('admin_books'))

    form.description.data = book.description
    form.name.data = book.name
    return render_template('admin/book.html', action="Edit",
                           add_book=add_book, form=form,
                           book=book, title="Edit Book")


@app.route('/admin/book/delete/<int:id>', methods=['GET', 'POST'], endpoint='admin_delete_book')
@login_required
def delete_book(id):
    """
    Delete a department from the database
    """
    check_admin()

    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    flash('You have successfully deleted the book.')

    # redirect to the departments page
    return redirect(url_for('admin_books'))