#!/bin/sh
cd /srv/flask-minimal
. .venv/bin/activate
waitress-serve app:app