import requests
import json


def test_get_headers_body_json():
    url = "https://petstore.swagger.io/v2/user/test"

    payload={}

    headers = {}


    resp = requests.get(url, headers=headers)

# Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 200
    print(resp.text)

test_get_headers_body_json()
