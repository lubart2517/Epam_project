from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField


CHOICES_SORT = (
    ("1", "Name_asc"),
    ("2", "Name_desc"),
    ("3", "Count_asc"),
    ("4", "Count_desc"),
)

CHOICES_FILTER = (
    ("1", "Author_name_contains="),
    ("2", "Count="),
    ("3", "Name_contains"),
    ("4", "Desc_contains"),
)


class BooksQueryForm(FlaskForm):
    """
    Form for admin to sort and find books
    """
    sort = SelectField('sort', choices=CHOICES_SORT)
    filter = SelectField('filter', choices=CHOICES_FILTER)
    find = StringField('find')
    submit = SubmitField('Sort&Filter')
