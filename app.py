from flask import Flask, jsonify, request
import controller

from datetime import datetime
from db import create_table

app = Flask(__name__)


@app.route('/')
def index():
    resp = {
        "api": "v1.0",
        "message": "welcome to the store!"
    }
    return jsonify(resp), 200


@app.route('/store', methods=["GET"])
def get_items():
    try:
        items = controller.get_items()
        total_price, total_tax = 0.0, 0.0
        res = []
        for item in items:
            total_tax += item[4]
            total_price += item[5]
            res.append({
                "item": item[1],
                "itemCategory": item[2],
                "price": item[3],
                "tax": item[4],
                "total": item[5],
                "quantity": item[6],
                "time": str(datetime.now())
            })

        if total_price > 2000.0:
            total_price -= (total_price*0.05)

        res = sorted(res, key=lambda x: x["item"])
        res += [{"totalPrice": total_price}, {"totalTax": total_tax}]
        return jsonify(res), 200
    except Exception as e:
        res = {"An exception occurred while processing the request": str(e)}
        return jsonify(res), 500


def validate_item(item):
    if "item" not in item:
        return False
    if "itemCategory" not in item:
        return False
    if "price" not in item:
        return False
    if "quantity" not in item:
        return False
    if item["itemCategory"] not in ("Book", "Medicine", "Food", "Clothes", "Music", "Imported"):
        return False
    if not ( isinstance(item["price"], int) or isinstance(item["price"], float) ):
        return False
    if not ( isinstance(item["quantity"], int) ):
        return False
    return True


@app.route("/store", methods=["POST"])
def insert_item():
    try:
        item_details = request.get_json()
        result = []
        for item in item_details:
            if not validate_item(item):
                return jsonify([]), 503
            name = item["item"]
            category = item["itemCategory"]
            price = item["price"]
            quantity = item["quantity"]
            result.append( controller.insert_item(name, category, price, quantity))

        return jsonify(result), 201
    except Exception as e:
        res = {"An exception occured while processing the request": str(e)}
        return jsonify(res), 500


if __name__ == "__main__":
    create_table()
    """
    Here you can change debug and port
    Remember that, in order to make this API functional, you must set debug in False
    """
    app.run(host='0.0.0.0', port=8000, debug=False)
