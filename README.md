# psychtoday
### Author: George Mandella

https://github.com/chichitonaru/psychtoday.git

## Welcome to my submission for the Psychology Today API and UI code challenge for the QA Automation Engineer role.

### Introduction
For these test suites to run, I have created a virtual environment that contains the dependencies for the Python applications to run within. The bash scripts that run the test suites will activate and deactivate these. The list of dependencies is as follows:
* Python 3.9
* pytest
* Selenium
* requests (python library)

### Running the API Test Suite
* In order to run the API Test Suite, from the root "psychtoday" folder, change directories to the "api challenge" folder and simply run the bash script:
```bash
./test_api.sh
```

* If there is a permission denied error, the permissions may need to be changed so that the shell script can be executed:
```bash
chmod +x test_api.sh
```

## Descriptions of API Test Cases
### 1. test_card_database_version_endpoint  
  * **test_get_check_database_version**
    * This test verifies that the database version is in the 20s and that it was last updated this month, this year. Since I have no control over when this API is updated, I figured the version number wouldn't update past a major version (20.XX) and even if it did update, it would only be during this month during the period of time I am completing this code challenge for my interview process.
  * **test_get_check_database_version_error**
    * In the API documentation, it is explained that the API will return an error if any GET parameters are sent to this endpoint, so I verify this by purposefully sending GET parameters and verifying I get an error message back with a 400 status code.

### 2. test_card_archetypes_endpoint  
  * **test_get_all_card_archetypes**
    * This test verifies that the database returns all the recognized archetypes for the cards in the Yu-Gi-Oh card game. An "archetype" in Yu-Gi-Oh is something like a "super-class" that a card can have, allowing them to interact and be interacted with by cards from the same parent group of cards. As card archetypes are added to the database, I wanted the test case to continue to pass even if new archetypes are introduced before the submission of this exercise, thus I verify if the length of the returned list is greater than or equal to the current 390 different archetypes. To verify that the database isn't losing archetypes, I also verify some of the most famous archetypes are found within the parsed/dumped JSON string. Instead of looping through the entire list, I dump the JSON to a string and verify that I can find the well-known archetype names within that dumped string as that is faster than checking every index.
  * **test_get_all_card_archetypes_error**
    * Similar to the test_card_database_version_error test, this test verifies that the API will return an error if any GET parameters are sent to this endpoint. I verify this by purposefully sending GET parameters and then checking I get an error message back with a 400 status code.

### 3. test_card_set_information_endpoint  
  * **test_get_card_set_information_specific**
    * This test verifies that a single card overview is provided given a specific "setcode" parameter. It checks the "id", "name", "set_name", "set_code", "set_rarity", and "set_price" are returned and does some validation on the returned values.
  * **test_get_card_set_information_no_setcode_error**
    * This test verifies that an error is returned when no 'setcode' is sent to the API.
  * **test_get_card_set_information_invalid_parameter_error**
    * This test verifies that an error is returned when an invalid parameter, in this case 'petcode', is sent to the API.
  * **test_get_card_set_information_invalid_card_error**
    * This test verifies that an error is returned when a 'setcode' is sent that doesn't match an existing card is sent to the API.

### 4. test_card_set_list_endpoint
  * **test_get_all_card_sets**
    * This test verifies that the returned JSON of all the card sets contains the names of a handful of Yu-Gi-Oh card sets released throughout the game's 20+ year-old history. It also verifies that if more card sets are added (and not subtracted), the amount of sets should total over 860.
  * **test_get_all_card_sets_error**
    * In the API documentation, it is explained that the API will return an error if any GET parameters are sent to this endpoint, so I verify this by purposefully sending GET parameters and verifying I get an error message back with a 400 status code.
