FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

ADD requirements.txt /code/

RUN pip install -r requirements.txt

ADD . /code/

#uWSGI will list on this port
EXPOSE 8000

# Add any custom, static enviroment variables needed by Django or your settings file here:
ENV DJANGO_SETTINGS_MODULE=composeexample.settings.deploy
