#!/usr/bin/env bash
# create_fixtures.sh

# make sure you ran `pip install django-fixture-magic` and added `'fixture_magic'` to INSTALLED_APPS
source env/bin/activate

echo "create fixtures_stelle"
python manage.py dump_object archiv.stelle 808 860 > fixtures_stelle.json

echo "create fixtures_spatialcoverage"
python manage.py dump_object archiv.spatialcoverage 4 5 > fixtures_spatialcoverage.json

echo "create fixtures_keyword"
python manage.py dump_object archiv.keyword 28 > fixtures_keyword.json

echo "create fixtures_layer"
python manage.py dump_object layers.geojsonlayer 7 3 > fixtures_layer.json

echo "merging fixtures"
python manage.py merge_fixtures fixtures_stelle.json fixtures_spatialcoverage.json fixtures_keyword.json fixtures_layer.json > archiv/fixtures/dump.json

echo "delete fixtures"
rm fixtures_keyword.json
rm fixtures_spatialcoverage.json
rm fixtures_stelle.json
rm fixtures_layer.json

echo "done"