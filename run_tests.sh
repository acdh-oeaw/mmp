#!/usr/bin/env bash

source env/bin/activate
coverage run manage.py test archiv --settings=djangobaseproject.settings.pg_local
coverage html
xdg-open htmlcov/index.html