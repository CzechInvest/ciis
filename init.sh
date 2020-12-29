#!/bin/bash

service ssh start

#python3 -m http.server 9000 
gunicorn -b 0.0.0.0:9000 --error-logfile /var/ciis/logs/error.log ciis.wsgi

