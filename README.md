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

I have included the chromedriver for Mac in the repo, but it requires that Chrome be installed on the host system running the tests. The only setup that should be required to run the UI tests should be to have Chrome installed if it isn't already. If the Chrome on the host machine doesn't match the chromedriver I've included in the repo, the matching chromedriver will need to be downloaded on the host system, too.
* Initially, I had planned to run the UI tests in Docker to alleviate these dependencies, but was having difficulty getting the tests to run inside the container.
* I was able to spin up a container with the dependencies (Chrome, chromedriver, python, selenium, the test files, etc.), but the tests wouldn't run and output any results.

### Running the API Test Suite
* In order to run the API Test Suite, from the root "psychtoday" folder, change directories to the "api_challenge" folder and simply run the bash script:
```bash
./test_api.sh
```

* If there is a permission denied error, the permissions may need to be changed so that the shell script can be executed:
```bash
chmod +x test_api.sh
```

### Running the UI Test Suite
* In order to run the UI Test Suite, from the root "psychtoday" folder, change directories to the "ui_challenge" folder and simply run the bash script:
```bash
./test_ui.sh
```

* If there is a permission denied error, the permissions may need to be changed so that the shell script can be executed:
```bash
chmod +x test_ui.sh
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

### 5. test_random_card_endpoint  
  * **test_get_random_card**
    * This test obtains a random card from the random card endpoint and verifies that the card has an 'id', 'name', and 'desc'.
  * **test_get_random_card_cross_reference**
    * This test obtains a random card from the random card endpoint and then uses the 'id' from that random card to get the same card using the card info endpoint. The two cards are compared against each other to verify that the same card was obtained from both endpoints.
  * **test_get_random_card_error**
    * Similar to the test_card_database_version_error test, this test verifies that the API will return an error if any GET parameters are sent to this endpoint. I verify this by purposefully sending GET parameters and then checking I get an error message back with a 400 status code.

## Descriptions of UI Test Cases  
### 1. test_landing_page_smoke  
  * **test_headers_and_links**
    * This test checks for the presence of important headers and links found on the Psychology Today front page in the US.

### 2. test_find_a_therapist  
  * **test_therapist_search**
    * This test does a simple check of searching for a city name and validates a search page is returned with the correct city and state with little information supplied to the engine.
