#!/usr/bin/env bash
# create_fixtures.sh

# make sure you ran `pip install django-fixture-magic` and added `'fixture_magic'` to INSTALLED_APPS
source env/bin/activate

echo "create fixtures_stelle"
python manage.py dump_object archiv.stelle 808 860 --settings=djangobaseproject.settings.pg_local > fixtures_stelle.json

echo "create fixtures_spatialcoverage"
python manage.py dump_object archiv.spatialcoverage 4 --settings=djangobaseproject.settings.pg_local > fixtures_spatialcoverage.json

echo "create fixtures_keyword"
python manage.py dump_object archiv.keyword 28 --settings=djangobaseproject.settings.pg_local > fixtures_keyword.json

echo "merging fixturs"
python manage.py merge_fixtures fixtures_stelle.json fixtures_spatialcoverage.json fixtures_keyword.json --settings=djangobaseproject.settings.pg_local > archiv/fixtures/dump.json

echo "delete fixtures"
rm fixtures_keyword.json
rm fixtures_spatialcoverage.json
rm fixtures_stelle.json

echo "done"