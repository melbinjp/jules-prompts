"""The HTTP interface the web app uses."""
from http import HTTPStatus

import store


def post_bookings(body):
    try:
        store.create(body)
    except Exception:
        return HTTPStatus.CONFLICT, {}
    return HTTPStatus.CREATED, {}


def get_bookings(query):
    return HTTPStatus.OK, [{"id": i, "slot": s} for i, s in store.upcoming(query["phone"])]


def delete_booking(booking_id):
    store.cancel(booking_id)
    return HTTPStatus.NO_CONTENT, {}
