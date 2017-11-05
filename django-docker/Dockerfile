FROM python:3.6

ENV PYTHONUNBUFFERED 1

# install required packages
RUN brew update && \
    brew upgrade -y && \
    brew install -y \
        git \
        python3 \
        python3-dev \
        python3-setuptools \
        python3-pip \
        nginx \
        supervisor \
        sqlite3 && \
        pip3 install -U setuptools && \

RUN mkdir /code

WORKDIR /code

ADD requirements.txt /code/

RUN pip install -r requirements.txt

ADD . /code/

#uWSGI will list on this port
EXPOSE 8000

# Add any custom, static enviroment variables needed by Django or your settings file here:
ENV DJANGO_SETTINGS_MODULE=composeexample.settings.deploy
