#!/bin/bash

while ! psql --host=opd_postgres --username=postgres > /dev/null 2>&1; do
    echo 'Waiting for connection with PostgreSQL ...'
    sleep 1;
done;
echo 'Successfully connected to PostgreSQL';

python manage.py migrate
python manage.py runserver 0.0.0.0:80
