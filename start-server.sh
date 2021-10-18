#!/usr/bin/env bash
# start-server.sh

echo "changed owner test"

if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (echo "creating superuser ${DJANGO_SUPERUSER_USERNAME}" && python djangobaseproject/manage.py createsuperuser --no-input --noinput --email 'blank@email.com' --settings=djangobaseproject.settings.docker)
fi
cd djangobaseproject && python manage.py collectstatic --no-input --settings=djangobaseproject.settings.docker &&
gunicorn djangobaseproject.wsgi_docker --bind 0.0.0.0:8010 --workers 3 & nginx -g "daemon off;"
