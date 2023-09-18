#!/usr/bin/env bash

# exit on error
set -o errexit
# install dependnecies
pip install -r dependencies.txt
# run migrations in case any migrations hadn't been run yet
python3 manage.py migrate

