import json
import requests

endpoint = "https://db.ygoprodeck.com/api/v7/cardsetsinfo.php"

def test_get_card_set_information_specific():
    print("\n[test_get_card_set_information_specific]")
    response = requests.get(endpoint, {"setcode": "SDY-006"})
    card_set_json = response.json()
    dumped = json.dumps(card_set_json, indent=4)

    print("Asserting Status Code 200")
    assert response.status_code == 200
    print("Asserting 'id' parameter == 46986421")
    assert card_set_json['id'] == 46986421
    print("Asserting 'name' parameter == 'Dark Magician'")
    assert card_set_json['name'] == 'Dark Magician'
    print("Asserting 'set_name' parameter == 'Starter Deck: Yugi'")
    assert card_set_json['set_name'] == 'Starter Deck: Yugi'
    print("Asserting 'set_code' parameter == 'SDY-006 '")
    assert card_set_json['set_code'] == 'SDY-006'
    print("Asserting 'set_rarity' == 'Ultra Rare'")
    assert card_set_json['set_rarity'] == 'Ultra Rare'
    print("Asserting 'set_price' in dumped JSON")
    assert 'set_price' in dumped

def test_get_card_set_information_no_setcode_error():
    print("\n[test_card_set_information_no_setcode_error]")
    response = requests.get(endpoint)
    parsed = json.loads(response.content)

    print("Asserting Status Code 400")
    assert response.status_code == 400
    print("Asserting 'error' in parsed JSON")
    assert 'error' in parsed

def test_get_card_set_information_invalid_parameter_error():
    print("\n[test_get_card_set_information_invalid_parameter_error]")
    response = requests.get(endpoint, {'petcode': 'SDY-006'})
    parsed = json.loads(response.content)

    print("Asserting Status Code 400")
    assert response.status_code == 400
    print("Asserting 'error' in parsed JSON")
    assert 'error' in parsed

if __name__ == '__main__':
    test_get_card_set_information_specific()
    test_get_card_set_information_no_setcode_error()
    test_get_card_set_information_invalid_parameter_error()

    print('END OF LINE.')
