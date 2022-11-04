# Contributing

## How to set up a development environment with VS Code

- start dev container in vs code
- on initial run, apply db dump to postgres database:
  ```
  cat mmp-db-dump.sql | docker exec -i mmp_devcontainer-db-1 psql -U mmp -W postgres -d mmp
  ```
- in dev container console, run
  ```
  pip install -r requirements.txt
  pip install https://github.com/diyclassics/latin-spacy-models/blob/main/la_core_cltk_sm/la_core_cltk_sm-0.1.0.tar.gz\?raw\=true
  python manage.py runserver
  ```