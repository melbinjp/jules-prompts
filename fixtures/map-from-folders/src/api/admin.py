from flask import Blueprint, request

from pantry.db import connection

bp = Blueprint("admin", __name__)


@bp.post("/admin/prices/<sku>")
def set_price(sku):
    with connection() as db:
        db.execute("UPDATE prices SET price = %s WHERE sku = %s", (request.json["price"], sku))
    return "", 204
