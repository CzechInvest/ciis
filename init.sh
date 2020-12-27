#!/bin/bash

service ssh start

gunicorn -b 0.0.0.0:9000 --error-logfile /var/ciis/logs/error.log ciis.wsgi

