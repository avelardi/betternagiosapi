from python:3-alpine

ADD requirements.txt .

RUN apk add --no-cache python3-dev build-base linux-headers \
 && pip install -r requirements.txt

ADD app app

CMD ["uwsgi", "--http", ":9090", "--wsgi-file", "app/app.py"]
