from python:3-alpine

ADD requirements.txt .

RUN apk add --no-cache python3-dev build-base linux-headers pcre-dev \
 && pip install -r requirements.txt

WORKDIR /app

ADD app .

CMD ["uwsgi", "--http", ":9090", "--wsgi-file", "wsgi.py"]
