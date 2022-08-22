from urllib import response
from app.config import *

def test_status():
    response=client.get("/status")
    data=response.json()
    assert response.status_code==200
    assert data["message"]=="ok"


def test_get_item():
    response=client.get("/items/l")
    data=response.json()
    assert response.status_code==200
    assert data.get("id")==1
    assert data.get("title")=="test"
    assert data.get("description")=="ok"
