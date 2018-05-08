# NagiosAPI

## Requirements

- A running Nagios instance.
- Docker (Optional)

## Installation

```sh
$ git clone git@github.com:rmcintosh/NagiosAPI.git
$ cd NagiosAPI
```

From there you can choose to run it as a standard python applicaiton, or with Docker.

### Standard

```sh
$ pip install -r requirements.txt
$ cd app/
$ export NAGIOS_STATUS_PATH=/usr/local/nagios/var/status.dat
$ uwsgi --http :9090 --wsgi wsgi:application --master
```

### Docker

```sh
$ docker build -t rmcintosh/nagios-api .
$ docker run -d \
    -p 9090:9090 \
    -e NAGIOS_STATUS_PATH=/usr/local/nagios/var/status.dat \
    -v /usr/local/nagios/var/status.dat:/usr/local/nagios/var/status.dat
    rmcintosh/nagios-api
```
