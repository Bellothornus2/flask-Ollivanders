from flask import redirect, Blueprint, request
from services import post_items,get_last_id,get_item

post_item_blue = Blueprint("post_item", __name__)


@post_item_blue.route("/item", methods=["POST"])
def post_item():
    data = request.get_json()
    name = data["name"]
    sell_in = data["sell_in"]
    quality = data["quality"]
    post_items.post_item(name, int(sell_in), int(quality))
    last_id = str(get_last_id.get_last_id())
    answer = get_item(last_id)
    return answer
