#/bin/bash

cd /home/hector/sites/superlists-staging-adler/source
../virtualenv/bin/gunicorn --bind unix:/tmp/superlists-staging-adler.socket superlists.wsgi:application

