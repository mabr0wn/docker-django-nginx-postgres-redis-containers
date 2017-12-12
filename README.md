[![Docker Pulls](https://img.shields.io/docker/pulls/mashape/kong.svg)]() [![Docker Build Status](https://img.shields.io/docker/build/jrottenberg/ffmpeg.svg)]() [![PyPI](https://img.shields.io/pypi/pyversions/Django.svg)]() [![GitHub language count](https://img.shields.io/github/languages/count/badges/shields.svg)]()

![alt text](https://realpython.com/images/blog_images/dockerizing-django/django-docker.png)

[Docker](https://www.docker.com/) is a containerization tool used for spinning up isolated, reproducible application enviroments. **This piece detials how to containerize a Django Project, Postgres, and Redis for local development along with delivering the stack to the cloud via [Docker Compose](https://docs.docker.com/compose/) and [Docker Machine](http://docs.docker.com/machine/)


In the end, the stack will include a separate container for each service:

- 1 web/Django container
- 1 nginx container
- 1 Postgres container
- 1 Redis container
- 1 data container

![alt text](https://realpython.com/images/blog_images/dockerizing-django/container-stack.png)

### Updates:
- *11/10/2017*: Added named data volumes to the Postgres and Redis containers.
- *11/13/2017*: Added Docker Toolbox, and also updated to the latest versions of Docker - Docker client(17.09.0-ce, build afdb6d4), Docker composer (v1.16.1, build 6d1ac21), Docker Machine(v0.12.2, build 9371605)

# Django-Docker
Build a simple web app using Django with Docker
# 1. Install Docker for Mac
The first step is to install the [Docker for Mac](https://www.docker.com/docker-mac) or [Docker for Windows](https://www.docker.com/docker-windows) if that's your cup of tea.

# 2. Get familiar with Docker
Open a shell (using an application like Terminal or iTerm), and run the following command:

```
docker run -it ubuntu:16.04 bash
```

Let's take a look at what this command does.

The **docker run** command lets you start a container from an image. In this case, you are creating a container from the **ubuntu:16.04** image. This is the **ubuntu** image with the **16.04** tag.

Each Docker container should run a single process. So the **docker run** command lets you specify a single command to run inside of the container. In our case, we are going to run a **bash** shell. So we've specified the command to run as bash. Since we are running a bash shell we are going to want to allocate a pseudo-TTY and keep STDIN open. This is why we've added the options **-it** to the run command.

After running this command you should see something like this:

```
root@69129699ac86:/#
```

This is the bash shell running inside of the container you just created from the ubuntu image. You can run **ps** to see which processes are running in this container.

```
root@69129699ac86:/# ps
  PID TTY          TIME CMD
    1 ?        00:00:00 bash
   18 ?        00:00:00 ps
```


Type **exit** to close the shell. Now you can run **docker ps** to see which containers are currently running. You should find that there are no running containers. But if you run docker ps -a you'll see all containers including the one you just stopped. Since the containers are designed to run a single process, once that process is finished the container stops.

Take a look at the fields displayed by **docker ps -a.** Two important fields are **CONTAINER ID** and **NAMES**. If you want to interact with your containers you'll need to know the name or id.

If you want to start this container back up you can do so with **docker start -ai .** Since the COMMAND associated with this container is bash we need to attach STDIN, STDOUT, and STDERR, hence the **-ai** options.

Theoretically we could run our container in the background. If our command was something else, say **python manage.py runserver 0.0.0.0:8000**, we would likely want to run our container in the background. In this case we would be able to see our container running when we type **docker ps**. If we want to run a command on an existing container we will use the **docker exec** command. The exec command offers familiar options, so if we wanted to open a shell in our django container we could type **docker exec -it bash**.

# 3. Create your Dockerfile

For our Django app we're going to build a custom Django image. There is a lot to learn about Docker images in the future, so you should definitely read up on them when you're ready.

For this demo, you'll want to create a directory to store all of your files. I've created a directory called ~/repos/django-docker. You can do this with:

```cli
mkdir -p ~/repos/django-docker
```

and go to this directory:

```cd ~/repos/django-docker```

Now create a file in this directory called **Dockerfile.**

```touch Dockerfile```

Then edit this file in your favorite editor. Add the following to Dockerfile:

```
FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

ADD requirements.txt /code/

RUN pip install -r requirements.txt


ADD . /code/
```

Check out the [Dockerfile reference](https://docs.docker.com/engine/reference/builder/) for more information about how to build a Dockerfile.

# 4. Create your requirements.txt file

The requirements.txt file contains the python modules necessary to run your application. In this case when need to install Django and psycopg2 (postgres + python). The Dockerfile we created in the previous step will install these required modules.

```touch requirements.txt```
And open this file to edit. Add the following:

```
Django
psycopg2
```

# 5. Create your docker-compose.yml file

```touch docker-compose.yml```

And open this file to edit. Add the following:

```
version: '3.3'

services:
  db:
    image: postgres
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    depends_on:
      - db
See the compose file reference for more info.
```

# 6. Create your Django project

You'll need to use the docker-compose run command to start your Django project. Of course, if you've already got a project started this step is unnecessary, but it may still be helpful to read through.

In your docker-compose.yml file, we've specified the command we want to run as python manage.py runserver 0.0.0.0:8000. This is the command that will be run when we bring up our container using docker-compose up. But before we can get to that point, we actually need a Django project. To do this we'll need to run a command against our web service using docker-compose run.

```docker-compose run web django-admin.py startproject composeexample .```

# 7. Configure Django to connect to the database

Django's database settings are in the settings.py file located in your primary app directory - composeexample/settings.py. Go ahead and open this file to edit.

Search for DATABASES and ensure the configuration looks like this:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}
```

Notice the hostname. If you look back at your docker-compose file, this is the name of the database service we're creating. When we use docker compose to start up our services, a default network is created and our containers are able to reach each other on this network. Moreover, they are able to reach each other using a hostname that is identical to the service name.

# 8.Run docker-compose up
At this point we're ready to take a look at our empty application. Run docker-compose up to start the Django server.

docker-compose up
At this, you'll be able to view your site in the browser using [http://localhost:8000](http://localhost:8000).

# 9.Running tests

Running tests is fairly straight forward. You can run a basic test using the docker-compose run command.

```docker-compose run web python manage.py test```

But what if you want to automate the test? I was recently inspired to automate a test in my deploy script. So when running my deployment script, I would first spin up a docker container, run tests, and if the tests pass I can continue with the deployment. Otherwise, we stop and fix the issues.

I created a simple test script:

```
#!/bin/bash

python manage.py test --noinput 2> /var/log/test.log 1> /dev/null

if [ $? -ne 0 ]; then
    cat /var/log/test.log
    exit 1
fi
```

And then in my deployment script I added the following:

```
docker-compose run --rm web ./bin/test.sh

if [ $? -ne 0 ]; then
        echo "Tests did not pass! Fix it."
        exit 1
fi
```

The --rm flag removes the containers immediately after they stop.

