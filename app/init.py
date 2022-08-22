from urllib import response
from app.config import *

def test_status():
    response=client.get("/status")

    assert response.status_code==200
    data=response.json()
