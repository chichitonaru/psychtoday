#!/bin/bash

# Author: George Mandella

echo "================================================================================"
echo "Activating psych-env Virtual Environment"
source ../psych-env/bin/activate
echo "<Beginning UI Test Suite>"
rm -rf results
mkdir results

echo "[Test Psychology Today Landing Page Smoke]"
pytest tests/test_landing_page_smoke.py -s | tee results/test_landing_page_smoke.log
sleep 2.0s

echo "Deactivating psych-env Virtual Environment"
deactivate
echo "================================================================================"
echo "END OF LINE."
