#!/usr/bin/env bash

source env/bin/activate
source set_env_variables.sh
coverage run manage.py test archiv
coverage html
xdg-open htmlcov/index.html