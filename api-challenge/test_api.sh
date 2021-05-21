#!/bin/bash

# Author: George Mandella

echo "================================================================================"
echo "Activating psych-env Virtual Environment"
source ../psych-env/bin/activate
echo "<Beginning API Test Suite>"
rm -rf results
mkdir results
echo "https://db.ygoprodeck.com/api-guide/"

echo "[Test Card Database Version Endpoint]"
pytest tests/test_card_database_version_endpoint.py -s | tee results/test_card_database_version_endpoint.log
sleep 2.0s

echo "[Test Card Archetypes Endpoint]"
pytest tests/test_card_archetypes_endpoint.py -s | tee results/test_card_archetypes_endpoint.log
sleep 2.0s

echo "[Test Card Set Information Endpoint]"
pytest tests/test_card_set_information_endpoint.py -s | tee results/test_card_set_information_endpoint.log
sleep 2.0s

echo "[Test Card Set List Endpoint]"
pytest tests/test_card_set_list_endpoint.py -s | tee results/test_card_set_list_endpoint.log
sleep 2.0s

echo "[Test Random Card Endpoint]"
pytest tests/test_random_card_endpoint.py -s | tee results/test_random_card_endpoint.log
sleep 2.0s

echo "Building API Challenge Report"
python build-report.py

echo "Deactivating psych-env Virtual Environment"
deactivate
echo "================================================================================"
echo "END OF LINE."
