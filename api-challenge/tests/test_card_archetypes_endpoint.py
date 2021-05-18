import json
import requests

endpoint = "https://db.ygoprodeck.com/api/v7/archetypes.php"

def test_get_all_card_archetypes():
    print("\n[test_get_all_card_archetypes]")
    response = requests.get(endpoint)
    archetypes_json = response.json()
    dumped = json.dumps(archetypes_json, indent=4)

    print("Asserting Status Code 200")
    assert response.status_code == 200
    print("Asserting archetypes JSON length >= 390")
    assert len(archetypes_json) >= 390
    print("Asserting 'Black Luster Soldier' in dumped JSON")
    assert 'Black Luster Soldier' in dumped
    print("Asserting 'Blue-Eyes' in dumped JSON")
    assert 'Blue-Eyes' in dumped
    print("Asserting 'Dark Magician' in dumped JSON")
    assert 'Dark Magician' in dumped
    print("Asserting 'Forbidden' in dumped JSON")
    assert 'Forbidden' in dumped
    print("Asserting 'Magician Girl' in dumped JSON")
    assert 'Magician Girl' in dumped
    print("Asserting 'Red-Eyes' in dumped JSON")
    assert 'Red-Eyes' in dumped

def test_get_all_card_archetypes_error():
    print("\n[test_get_all_card_archetypes_error]")
    response = requests.get(endpoint, {'archetype': 'Error'})
    parsed = json.loads(response.content)

    print("Asserting Status Code 400")
    assert response.status_code == 400
    print("Asserting 'error' in parsed JSON")
    assert 'error' in parsed

if __name__ == '__main__':
    test_get_all_card_archetypes()
    test_get_all_card_archetypes_error()

    print('END OF LINE.')
