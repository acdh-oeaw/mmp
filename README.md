[![Test](https://github.com/acdh-oeaw/mmp/actions/workflows/test.yml/badge.svg)](https://github.com/acdh-oeaw/mmp/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/acdh-oeaw/mmp/branch/master/graph/badge.svg?token=PQTAIJWOGX)](https://codecov.io/gh/acdh-oeaw/mmp)
[![flake8 Lint](https://github.com/acdh-oeaw/mmp/actions/workflows/lint.yml/badge.svg)](https://github.com/acdh-oeaw/mmp/actions/workflows/lint.yml)


# MMP

## Mapping Medieval Peoples: Visualizing Semantic Landscapes in Early Medieval Europe

### About

a generic djangobaseproject port of https://gitlab.com/acdh-oeaw/imafo/gens, created with following steps:

## Install

* clone the repo `git clone https://github.com/acdh-oeaw/mmp.git`
* [optional]
  * create a virtual env, e.g. `virtualenv myenv`
  * activate virtual env, e.g. `source myenv/bin/activate`
* install needed packages `pip install -r requirements.txt` (jupyter notebook requirements not incldued)
* [optional]
  * created your custom settings-file, e.g. `pg_local`

## Start

### on a clear database
* apply migrations `python manage.py migrate --settings=djangobaseproject.settings.dev`
* start dev-server `python manage.py runserver ---settings=djangobaseproject.settings.dev`
* open http://127.0.0.1:8000/

### use a db-dumpt

* get a dump
* create a new postgres-db name e.g. `mmp`
* create postgis-extension
* restore db-dump
* make sure your (local) settings-file matches your db-settings (should be the case if you use the checked in pg_local.py settings file and if you named your db `mmp`)
* start dev-server `python manage.py runserver ---settings=djangobaseproject.settings.pg_local`

[optional] populate netvis-cache

* run something like `python manage.py populate_netvis_cache <app_name> <model_name>`
  * `python manage.py populate_netvis_cache archiv autor --settings=djangobaseproject.settings.pg_local`

* go to http://127.0.0.1:8000/netvis/archiv/autor to the see the corresponding generic netvis


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
