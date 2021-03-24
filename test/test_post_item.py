import pytest
from app import app


@pytest.mark.post_item
def test_add_item():
    test = app.test_client()
    test.get("/add/item/hola/2/3")
    response = test.get("/")
    assert b'{"name":"hola","quality":3,"sell_in":2}' in response.data