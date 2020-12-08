#!/bin/sh

echo "starting the application"

python app.py run

exec "$@"