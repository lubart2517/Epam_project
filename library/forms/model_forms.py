from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from ..models.author_models import Author
from library import db


class BookForm(FlaskForm):
    """
    Form for admin to add or edit a book
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    count = SelectField('Count', choices=[x for x in range(10)], validators=[DataRequired()])
    author = SelectField('Author', choices=list(Author.query.all()), validators=[DataRequired()])
    submit = SubmitField('Submit')


class BookFormAddAuthor(FlaskForm):
    """
    Form for admin to add Author to the book
    """
    author = SelectField('Author', choices=[], validators=[DataRequired()])
    submit = SubmitField('AddAuthor')

    def __init__(self, author_choices: list = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if author_choices:
            self.author.choices = author_choices


class BookFormDeleteAuthor(FlaskForm):
    """
    Form for admin to add Author to the book
    """
    author = SelectField('Author', choices=[], validators=[DataRequired()])
    submit = SubmitField('DeleteAuthor')

    def __init__(self, author_choices: list = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if author_choices:
            self.author.choices = author_choices