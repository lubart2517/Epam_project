"""
order service used to make database queries, this module defines the
following classes:
- `OrderService`
"""

from library import db
from ..models.order_models import Order
import datetime

class OrderService:
    """
    order service used to make database queries
    """
    @staticmethod
    def get_orders():
        """
        Fetches all of the orders from database
        :return: list of all orders
        """

        return Order.query.all()

    @staticmethod
    def get_order_by_id(order_id):
        """
        Fetches the order with given ID from database, raises
        ValueError if such order is not found
        :param order_id: ID of the order to be fetched
        :raise ValueError: in case of order with given ID being absent
        in the database
        :return: order with given ID
        """
        order = Order.query.get_or_404(order_id)
        if order is None:
            raise ValueError('Invalid order id')
        return order

    @staticmethod
    def get_orders_by_user(user_id):
        """
        Fetches the orders with given user_id   from database,
        raises ValueError if such user_id is not found
        :param user_id: user_id of the orders to be fetched
        :return: orders made by user wirh given user_id
        """
        return db.session.query(Order).filter_by(
            user_id=user_id)

    @staticmethod
    def get_orders_by_book(book_id):
        """
        Fetches the orders with given book_id   from database,
        raises ValueError if such book_id is not found
        :param book_id: book_id of the orders to be fetched
        :return: orders made by user with given book_id
        """
        return db.session.query(Order).filter_by(
            book_id=book_id)

    @staticmethod
    def get_open_orders():
        """
        Fetches all of the opened orders  from database
        :return: list of all opened orders
        """
        return db.session.query(Order).filter_by(
            closed=True)

    @classmethod
    def close_order(cls, order_id):
        """
        Set value of closed field to True
        :return: order
        """
        order = cls.get_order_by_id(order_id)
        order.closed = True
        order.end_at = datetime.datetime.now()
        db.session.add(order)
        db.session.commit()
        return order

    @staticmethod
    def get_open_orders_by_user(user_id):
        """
        Fetches all of the opened orders  with given user_id from database
        :return: list of all opened orders by some user
        """
        return db.session.query(Order).filter_by(
            closed=True, user_id=user_id)

    @staticmethod
    def add_order_from_json(schema, order_json):
        """
        Deserializes order and adds it to the database
        :param schema: schema to be used to deserialize the order
        :param order_json: data to deserialize the order from
        :return: order that was added
        """
        order = schema.load(order_json, session=db.session)
        db.session.add(order)
        db.session.commit()
        return order

    @staticmethod
    def add_order(user_id, book_id):
        """
        Adds order to the database
        :param user_id: order user_id
        :param book_id: order book_id
        :return: order that was added
        """
        order = Order( user_id, book_id)
        db.session.add(order)
        db.session.commit()
        return order
