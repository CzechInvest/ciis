FROM ubuntu:18.04
LABEL vendor="CzechInvest"


RUN apt-get update && apt-get install -y locales python3 \
        gdal-bin python3-gdal libgdal-dev libsqlite3-mod-spatialite \
        nginx \
        python3-pip && rm -rf /var/lib/apt/lists/* \
        && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8

ENV PYTHONUNBUFFERED 1
ENV LANG en_US.utf8


ADD requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt
RUN pip3 install gunicorn

EXPOSE 8000
CMD  gunicorn ciis.wsgi
