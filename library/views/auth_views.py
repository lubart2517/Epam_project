from flask import flash, redirect, render_template, url_for, request
from flask_login import login_required, login_user, logout_user
from library import app, db
from ..forms.auth_forms import LoginForm, RegistrationForm
from ..models.user_models import User


@app.route('/register', methods=['GET', 'POST'], endpoint='register')
def register():
    """
    Handle requests to the /register route
    Add an user to the database through the registration form
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                            username=form.username.data,
                            first_name=form.first_name.data,
                            last_name=form.last_name.data,
                            password=form.password.data)

        # add user to the database
        db.session.add(user)
        db.session.commit()
        flash('You have successfully registered! You may now login.')

        # redirect to the login page
        return redirect(url_for('login'))

    # load registration template
    return render_template('auth/register.html', form=form, title='Register')


@app.route('/login', methods=['GET', 'POST'], endpoint='login')
def login():
    """
    Handle requests to the /login route
    Log an user in through the login form
    """
    form = LoginForm()
    if form.validate_on_submit():

        # check whether user exists in the database and whether
        # the password entered matches the password in the database
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.check_password(
                form.password.data):
            # log user in
            login_user(user)

            # redirect to the homepage after login
            if user.role:
                return redirect(url_for('admin_dashboard'))
            else:
                return redirect(url_for('homepage'))

        # when login details are incorrect
        else:
            flash('Invalid email or password.')

    # load login template
    return render_template('auth/login.html', form=form, title='Login')


@app.route('/logout', endpoint='logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log an user out through the logout link
    """
    logout_user()
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('login'))


