import json
import requests

endpoint = "https://db.ygoprodeck.com/api/v7/checkDBVer.php"

def test_get_check_database_version():
    print("\n[test_get_check_database_version]")
    response = requests.get(endpoint)
    parsed = json.loads(response.content)

    print("Asserting Status Code 200")
    assert response.status_code == 200
    print("Asserting '20.' in parsed JSON")
    assert '20.' in parsed[0]['database_version']
    print("Asserting '2021-05-' in parsed JSON")
    assert '2021-05-' in parsed[0]['last_update']

def test_get_check_database_version_error():
    print("\n[test_get_check_database_version_error]")
    response = requests.get(endpoint, {'database_version': '20.72'})
    parsed = json.loads(response.content)

    print("Asserting Status Code 400")
    assert response.status_code == 400
    print("Asserting 'error' in parsed JSON")
    assert 'error' in parsed

if __name__ == '__main__':
    test_get_check_database_version()
    test_get_check_database_version_error()

    print('END OF LINE.')
