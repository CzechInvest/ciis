FROM ubuntu:20.04
LABEL vendor="CzechInvest"

ENV SSH_PASSWD "root:An0quaweemsAj%"

RUN apt-get update && DEBIAN_FRONTEND="noninteractive" apt-get install -y locales python3 \
        gdal-bin python3-gdal libgdal-dev libsqlite3-mod-spatialite \
        openssl openssh-server lsb-release apt-utils wget \
        python3-pip && rm -rf /var/lib/apt/lists/* \
        && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias \
        en_US.UTF-8 && echo "$SSH_PASSWD" | chpasswd

COPY sshd_config /etc/ssh/

COPY init.sh /usr/local/bin/
RUN chmod u+x /usr/local/bin/init.sh

RUN echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -

RUN apt-get update && apt-get install -y postgresql-client-11

ENV PYTHONUNBUFFERED 1
#ENV DJANGO_SETTINGS_MODULE=settings_local
ENV LANG en_US.utf8
WORKDIR /var/ciis



ADD requirements.txt /tmp/requirements.txt
#RUN python3 /var/ciis/manage.py collectstatic --noinput
RUN pip3 install Cython
RUN pip3 install -r /tmp/requirements.txt
RUN pip3 install gunicorn
RUN mkdir -p /var/ciis/logs

ADD . /var/ciis/

EXPOSE 9000 2222
#EXPOSE 443

#CMD init.sh
ENTRYPOINT ["init.sh"]
#CMD bash
