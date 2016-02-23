#
#   ## 1. build container
#      docker build -t opd_python .
#
#   ## 2. clone opd-product-browser-web repo
#      git clone https://github.com/okfn/opd-product-browser-web.git
#
#   ## 3. install Modules required by the opd-product-browser-web repo
#      RUN pip install -r requirements.txt
#
#   ## ??? run website pointing to location of repo, linking to the PostgreSQL container
#      ??????????? docker run -d -p 18080:80 --link opd_db:opd_db --name opd_web -v <path-to-repo>/explorer/:/var/www/html/ opd_python

# Python:3.5 --------------------------------------------------------------
# This Dockerfile starts with a Python 3.5 base image. The base image is modified by adding a new code directory. The base image is further modified by installing the Python requirements defined in the requirements.txt file.
# See https://docs.docker.com/compose/django/

FROM python:3.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
