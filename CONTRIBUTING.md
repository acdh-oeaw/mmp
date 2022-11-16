# Contributing

## How to set up a development environment with VS Code

- start dev container in vs code
- on initial run, apply db dump to postgres database:
  ```
  cat mmp-db-dump.sql | docker exec -i mmp_devcontainer-db-1 psql -U mmp -W postgres -d mmp
  ```
  a current dump can be downloaded from [here](https://oeawacat.sharepoint.com/:u:/s/ACDH-CH_p_MappingMedievalPeoples_MMP/Eep7cp6jpztKjM1wDt2_RGwBE2g_dB9VDoNNbDQgnLUppA?e=uiBrb2).
- in dev container console, run
  ```
  pip install -r requirements.txt
  pip install https://github.com/diyclassics/latin-spacy-models/blob/main/la_core_cltk_sm/la_core_cltk_sm-0.1.0.tar.gz\?raw\=true
  DEBUG=True python manage.py runserver
  ```
