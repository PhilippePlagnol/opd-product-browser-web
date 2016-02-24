# See https://docs.docker.com/compose/django/

FROM python:3.5
ENV PYTHONUNBUFFERED 1

# Install postgresql-client to check if PostgreSQL is running
RUN \
  apt-get update && \
  apt-get install -yq --no-install-recommends postgresql-client && \
  apt-get clean

RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/
RUN pip install -r requirements.txt

ADD . /code/
