FROM ubuntu:18.04
LABEL vendor="CzechInvest"


RUN apt-get update && apt-get install -y locales apache2 \
        gdal-bin python3-gdal libgdal-dev libsqlite3-mod-spatialite \
        libapache2-mod-wsgi-py3 python3-pip && rm -rf /var/lib/apt/lists/* \
        && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8

ENV PYTHONUNBUFFERED 1
ENV LANG en_US.utf8


RUN mkdir /var/www/ciis
RUN mkdir /var/ciis
WORKDIR /var/ciis
ADD requirements.txt /var/ciis/
RUN pip3 install -r requirements.txt

ADD ciis-django.conf /etc/apache2/sites-available/
RUN a2ensite ciis-django
EXPOSE 80
ADD init_django-start_apache.sh /usr/local/bin/
CMD /bin/bash /usr/local/bin/init_django-start_apache.sh
