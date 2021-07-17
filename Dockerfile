FROM python:3.7-slim

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./
RUN apt-get update && \
  apt-get install -yq \
    python3 \
    python3-dev \
    python3-pip \
    python3-setuptools \
  && apt-get clean && rm -rf /var/lib/apt/lists/*
COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app