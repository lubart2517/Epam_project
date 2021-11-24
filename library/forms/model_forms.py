from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from ..models.author_models import Author
from library import db

class BookForm(FlaskForm):
    """
    Form for admin to add or edit a department
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    count = SelectField('Count', choices=[x for x in range(10)], validators=[DataRequired()])
    author = SelectField('Author', choices=[db.session.query(Author).all()], validators=[DataRequired()])
    submit = SubmitField('Submit')