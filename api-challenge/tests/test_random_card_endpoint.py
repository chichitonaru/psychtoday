import json
import requests

endpoint = "https://db.ygoprodeck.com/api/v7/randomcard.php"
xendpoint = "https://db.ygoprodeck.com/api/v7/cardinfo.php"

def test_get_random_card():
    print("\n[test_get_random_card]")
    response = requests.get(endpoint)
    random_card_json = response.json()
    dumped = json.dumps(random_card_json, indent=4)

    print("Asserting Status Code 200")
    assert response.status_code == 200
    print("Asserting 'id' in dumped JSON")
    assert 'id' in dumped
    print("Asserting 'name' in dumped JSON")
    assert 'name' in dumped
    print("Asserting 'desc' in dumped JSON")
    assert 'desc' in dumped

def test_get_random_card_cross_reference():
    print("\n[test_get_random_card]")
    response = requests.get(endpoint)
    random_card_json = response.json()
    dumped = json.dumps(random_card_json, indent=4)

    print("Asserting Status Code 200")
    assert response.status_code == 200
    random_id = random_card_json['id']
    random_name = random_card_json['name']
    random_desc = random_card_json['desc']

    print("Querying API for same random card via card info endpoint by 'id'")
    xresponse = requests.get(xendpoint, {'id': random_id})
    cross_card_json = xresponse.json()
    xdumped = json.dumps(cross_card_json, indent=4)

    print("Asserting Status Code 200")
    assert xresponse.status_code == 200
    cross_id = cross_card_json['data'][0]['id']
    cross_name = cross_card_json['data'][0]['name']
    cross_desc = cross_card_json['data'][0]['desc']
    print("Asserting random card 'id' " + str(random_id) + " == cross-referenced card 'id' " + str(cross_id))
    assert random_id == cross_id
    print("Asserting random card 'name' " + random_name + " == cross-referenced card 'name' " + cross_name  )
    assert random_name == cross_name
    print("Asserting random card 'desc' == cross-referenced card 'desc'")
    assert random_desc == cross_desc

def test_get_random_card_error():
    print("\n[test_get_random_card_error]")
    response = requests.get(endpoint, {'error': 'Error'})
    parsed = json.loads(response.content)

    print("Asserting Status Code 400")
    assert response.status_code == 400
    print("Asserting 'error' in parsed JSON")
    assert 'error' in parsed

if __name__ == '__main__':
    test_get_random_card()
    test_get_random_card_cross_reference()
    test_get_random_card_error()

    print('END OF LINE.')
