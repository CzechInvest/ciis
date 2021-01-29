#!/bin/bash

service ssh start

#python3 -m http.server 9000 

crontab -l > jobs.txt
echo "0 0 7 * * cd /var/ciis && python3 manage.py monthly_report \`date -d \"\$(date +%Y-%m-01) -1 day\" +'%Y-%m-%d'\`" >> jobs.txt
crontab jobs.txt

python3 manage.py migrate --settings settings.production
python3 manage.py collectstatic --settings settings.production

gunicorn -b 0.0.0.0:9000 --log-level debug --capture-output --log-file /var/ciis/logs/gunicorn.log --error-logfile /var/ciis/logs/error.log ciis.wsgi
