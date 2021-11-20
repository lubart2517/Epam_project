from flask import render_template


def users_index():
    users = [{'name': 'lol', 'count': '3'}]
    return render_template('users_index.html', users=users)


def users_overdue():
    users = [{'name': 'lol', 'count': '3'}]
    return render_template('users_overdue.html', users=users)