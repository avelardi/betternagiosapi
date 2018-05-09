from python:3-alpine

ADD requirements.txt .

RUN apk add --no-cache python3-dev build-base linux-headers pcre-dev \
 && pip install -r requirements.txt

WORKDIR /srv/nagiosapi

ADD nagiosapi .

CMD ["uwsgi", "--http", ":9090", "--uid", "10000", "--gid", "10000", "--wsgi", "wsgi:application", "--master"]
