from flask import Blueprint, request

from pantry.services import checkout

bp = Blueprint("orders", __name__)


@bp.post("/orders")
def place():
    return checkout.place_order(request.json)
