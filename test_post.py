import requests
import json


def test_post_headers_body_json():
    url = "https://petstore.swagger.io/v2/user"

    payload = json.dumps({
    "username": "test",
    "firstName": "sasha",
    "lastName": "vasha",
    "email": "string@twat.com",
    "password": "string",
    "phone": "2325626272",
    "userStatus": 0
})
    headers = {'Content-Type': 'application/json'}
    resp = requests.request("POST", url, headers=headers, data=payload)

    assert resp.status_code == 200
 

    print(resp.text)


test_post_headers_body_json()
