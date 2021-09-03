import requests
def test_delete_headers_body_json():
    url = "https://petstore.swagger.io/v2/user/test"

    payload={}
    headers = {}

    response = requests.request("DELETE", url, headers=headers, data=payload)
    assert response.status_code == 200
    print(response.text)
test_delete_headers_body_json()
