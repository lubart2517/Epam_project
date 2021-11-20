from flask import render_template


def orders_index():
    orders = [{'name': 'lol', 'count': '3'}]
    return render_template('orders_index.html', orders=orders)