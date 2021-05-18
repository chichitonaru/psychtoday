import json
import requests

endpoint = "https://db.ygoprodeck.com/api/v7/cardsets.php"

def test_get_all_card_sets():
    print("\n[test_get_all_card_sets]")
    response = requests.get(endpoint)
    card_sets_json = response.json()
    dumped = json.dumps(card_sets_json, indent=4)

    print("Asserting Status Code 200")
    assert response.status_code == 200
    print("Asserting card sets JSON length >= 860")
    assert len(card_sets_json) >= 860
    print("Asserting 'Starter Deck: Kaiba' in dumped JSON")
    assert 'Starter Deck: Kaiba' in dumped
    print("Asserting 'Duelist Pack: Yugi' in dumped JSON")
    assert 'Duelist Pack: Yugi' in dumped
    print("Asserting 'Code of the Duelist' in dumped JSON")
    assert 'Code of the Duelist' in dumped
    print("Asserting 'Genesis Impact' in dumped JSON")
    assert 'Genesis Impact' in dumped

def test_get_all_card_sets_error():
    print("\n[test_get_all_card_sets_error]")
    response = requests.get(endpoint, {'error': 'Error'})
    parsed = json.loads(response.content)

    print("Asserting Status Code 400")
    assert response.status_code == 400
    print("Asserting 'error' in parsed JSON")
    assert 'error' in parsed

if __name__ == '__main__':
    test_get_all_card_sets()
    test_get_all_card_sets_error()

    print('END OF LINE.')
