# MMP

## Mapping Medieval Peoples: Visualizing Semantic Landscapes in Early Medieval Europe

### About

a generic djangobaseproject port of https://gitlab.com/acdh-oeaw/imafo/gens, created with following steps:

### create custom app/datamodel

[data model is quite stable, so any further changes should happen in `archiv.models.py`]

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

* clone the repo `git clone https://github.com/acdh-oeaw/mmp.git`
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

[optional] populate netvis-cache

* run something like `python manage.py populate_netvis_cache <app_name> <model_name>`
  * `python manage.py populate_netvis_cache archiv autor --settings=djangobaseproject.settings.pg_local`

* go to http://127.0.0.1:8000/netvis/archiv/autor to the see the corresponding generic netvis

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


### building the image

`docker build -t mmp:latest .`
`docker build -t mmp:latest --no-cache .`

### running the image

To run the image you should provide an `.env` file to pass in needed environment variables; see example below:

```
DB_NAME=mmp
DB_USER=mmp
DB_PASSWORD=db_pw
PROJECT_NAME=mmp
SECRET_KEY=randomstring
DEBUG=True
DJANGO_SUPERUSER_USERNAME=user_name
DJANGO_SUPERUSER_PASSWORD=user_pw
VOCABS_DEFAULT_PEFIX=mmp
VOCABS_DEFAULT_PEFIX=en
REDMINE_ID=12345
```

`docker run -it -p 8020:8020 --rm --env-file .env_dev mmp:latest`

### or use published image:

`docker run -it -p 8020:8020 --rm --env-file .env_dev acdhch/mmp:latest`


### dev notes

`python manage.py remove_stale_contenttypes`