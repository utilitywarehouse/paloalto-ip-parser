FROM python:3.7-alpine
COPY requirements.txt /
RUN apk add python3-dev build-base linux-headers pcre-dev
RUN pip install -r /requirements.txt
COPY src/ /app
WORKDIR /app
CMD [ "uwsgi",  "--socket", "0.0.0.0:9090", "--wsgi-file=wsgi.py", "--protocol", "http", "-w", "wsgi:app",  "--processes", "4", "--threads", "2", "--stats", "127.0.0.1:9191" ]
