#!/usr/bin/env bash
# start-server.sh

echo "Hello from Project MMP"

uv run manage.py collectstatic --no-input 
uv run gunicorn djangobaseproject.wsgi --bind 0.0.0.0:8010 --workers 3 --timeout 600 & nginx -g "daemon off;"
