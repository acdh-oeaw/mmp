# gens django

## About

a generic djangobaseproject port of https://gitlab.com/acdh-oeaw/imafo/gens, created with following steps:

### create custom app/datamodel

* provide data-model mapping from gend-db-dump (gema_scire_2020-11-04.sql) as [gsheet](https://docs.google.com/spreadsheets/d/1A68SVvRjXECFHlDMcuUfE_BL2k7HfXFB9jQ-yr9EGdA/edit#gid=0)
* add the sheet-id to settings, e.g. `SHEET_ID = 'theidofthegsheetneedstobereadableforanyone-yr9EGdA`'
* run `python manage.py create_files --settings=djangobaseproject.settings.pg_local` to create application files:
  * data model
  * views

### import legacy data
* add legacy-db connection info to settings, e.g. 
```
LEGACY_DB_CONNECTION = {
    'NAME': 'legacy_db_name',
    'USER': 'legacy_db_user',
    'PASSWORD': 'legacy_db_pw',
    'HOST': 'localhost',
    'PORT': '3306'
}
```
* run script `python manage.py import_data --settings=djangobaseproject.settings.pg_local` to import data from legacy-db into djanog-db

## Install

* clone the repo `git clone https://gitlab.com/acdh-oeaw/imafo/gens-django.git`
* [optional]
  * create a virtual env, e.g. `virtualenv myenv`
  * activate virtual env, e.g. `source myenv/bin/activate`
* install needed packages `pip install -r requirements.txt` (jupyter notebook requirements not incldued)
* [optional]
  * created your custom settings-file, e.g. `pg_local`

## Start

* apply migrations `python manage.py migrate --settings=djangobaseproject.settings.dev`
* start dev-server `python manage.py runserver ---settings=djangobaseproject.settings.dev`
* open http://127.0.0.1:8000/

# ToDos

* write customize import scripts for few data points
* customize look of the application
* add API
  * which could be done in a generic way by expanding `appcreator` -> any new app created with this code would benefit from this

# included packages

## [acdh-django-browsing](https://github.com/acdh-oeaw/acdh-django-browsing)

Django-App providing some useful things to create browsing views


## [acdh-django-vocabs](https://github.com/acdh-oeaw/acdh-django-vocabs)

Curate controlled vocabularies as SKOS

## [acdh-django-geonames](https://github.com/acdh-oeaw/acdh-django-geonames)

A django package providing models and views for Geoname Places

* populate vocabs with geoname-feature codes
    * `python manage.py import_ftc --lang=en--settings=djangobaseproject.settings.dev`
* populate db with geoname-places of a given country:
    * `python manage.py import_places ..--country_code=YU--settings=djangobaseproject.settings.dev`
