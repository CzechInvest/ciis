FROM ubuntu:18.04
LABEL vendor="CzechInvest"


RUN apt-get update && apt-get install -y locales python3 \
        gdal-bin python3-gdal libgdal-dev libsqlite3-mod-spatialite \
        openssl \
        python3-pip && rm -rf /var/lib/apt/lists/* \
        && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=settings_local
ENV LANG en_US.utf8
WORKDIR /var/ciis


ADD requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt
RUN pip3 install gunicorn

EXPOSE 9000
EXPOSE 443

CMD  gunicorn -b 0.0.0.0:9000 --error-logfile /var/ciis/logs/error.log ciis.wsgi
#CMD bash
