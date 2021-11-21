from flask import render_template, redirect,url_for, flash
from flask_login import login_required, login_user, current_user, logout_user
from library import app, db
from ..models.user_models import User
from ..forms.user_forms import LoginForm


@login_required
def users_index():
    users = [{'name': 'lol', 'count': '3'}]
    return render_template('users_index.html', users=users)


@login_required
def users_overdue():
    users = [{'name': 'lol', 'count': '3'}]
    return render_template('users_overdue.html', users=users)


@app.route('/login/', methods=['post', 'get'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.query(User).filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('admin'))

        flash("Invalid username/password", 'error')
        return redirect(url_for('login'))
    return render_template('login.html', form=form)


@app.route('/logout/')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for('login'))