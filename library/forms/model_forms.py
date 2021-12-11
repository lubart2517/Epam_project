
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class BookFormInitial(FlaskForm):
    """
    Base class for all book forms
    """
    author = SelectField('Author', choices=[], validators=[DataRequired()])
    submit = SubmitField('Submit')

    def __init__(self, *args, author_choices: list = None, **kwargs):
        super().__init__(*args, **kwargs)
        if author_choices:
            self.author.choices = author_choices


class BookForm(BookFormInitial):
    """
    Form for admin to add or edit a book
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    count = SelectField('Count', choices=[*range(10)], validators=[DataRequired()])
    submit = SubmitField('Submit')


class BookFormAddAuthor(BookFormInitial):
    """
    Form for admin to add Author to the book
    """
    submit = SubmitField('AddAuthor')


class BookFormDeleteAuthor(BookFormInitial):
    """
    Form for admin to add Author to the book
    """
    submit = SubmitField('DeleteAuthor')


class AuthorForm(FlaskForm):
    """
    Form for admin to add or edit a book
    """
    name = StringField('Name', validators=[DataRequired()])
    middle_name = StringField('Middle name', validators=[DataRequired()])
    last_name = StringField('Lastname', validators=[DataRequired()])
    submit = SubmitField('Submit')
