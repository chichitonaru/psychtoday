#!/bin/bash

# Author: George Mandella

echo "================================================================================"
echo "Activating psych-env Virtual Environment"
source ../psych-env/bin/activate
echo "Pulling Docker Image for selenium/standalone-chrome"
docker pull selenium/standalone-chrome
echo "Starting Docker selenium/standalone-chrome:latest"
docker run -d -p 4444:4444 -v /dev/shm:/dev/shm selenium/standalone-chrome:latest
sleep 5.0s
echo "<Beginning UI Test Suite>"
rm -rf results
mkdir results

echo "[Test Psychology Today Landing Page Smoke]"
pytest tests/test_landing_page_smoke_docker.py -s | tee results/test_landing_page_smoke_docker.log
sleep 2.0s

echo "[Test Psychology Today Find a Therapist]"
pytest tests/test_find_a_therapist_docker.py -s | tee results/test_find_a_therapist_docker.log
sleep 2.0s

echo "[Test Psychology Today Login]"
pytest tests/test_login_docker.py -s | tee results/test_login_docker.log
sleep 2.0s

echo "Killing Docker Image"
docker kill $(docker ps -q)
echo "Removing Docker Container"
docker rm $(docker ps -a -q)

echo "Building UI Challenge Report"
python build-report.py

echo "Deactivating psych-env Virtual Environment"
deactivate
echo "================================================================================"
echo "END OF LINE."
