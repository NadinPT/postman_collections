import requests
import json


def test_put_headers_body_json():
    url = "https://petstore.swagger.io/v2/user/test"

    payload = json.dumps({
    "id": 0,
    "username": "sasha",
    "firstName": "sasha",
    "lastName": "vasha",
    "email": "string",
    "password": "string",
    "phone": "string",
    "userStatus": 0
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)


    assert response.status_code == 200
    print(response.text)

test_put_headers_body_json()
