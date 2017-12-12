[![Docker Pulls](https://img.shields.io/docker/pulls/mashape/kong.svg)]() [![Docker Build Status](https://img.shields.io/docker/build/jrottenberg/ffmpeg.svg)]() [![PyPI](https://img.shields.io/pypi/pyversions/Django.svg)]() [![GitHub language count](https://img.shields.io/github/languages/count/badges/shields.svg)]()

![alt text](http://yacows.com.br/media/images/2013/11/12/img-0-pythonninja.png)

[Docker](https://www.docker.com/) is a containerization tool used for spinning up isolated, reproducible application enviroments. **This piece details how to containerize a Django Project, Postgres, and Redis for local development along with delivering the stack to the cloud via** [Docker Compose](https://docs.docker.com/compose/) and [Docker Machine](http://docs.docker.com/machine/)


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

## Local Setup
Along with Docker(v17.09.0) we will be using -
  - [Docker Compose](v1.16.1) for orchestrating a multi-container application into a single app, and
  - [Docker Machine](v0.12.2) for creating Docker hosts both locally and in the cloud.
  
If you're running either Mac OS X or Windows, then download and install the [Docker Toolbox](https://www.docker.com/products/docker-toolbox) to get all the necessary tools. Otherwise follow the directions [here](https://docs.docker.com/compose/install/) and [here](https://docs.docker.com/machine/install-machine/) to install Docker Compose and Machine, respectively.

Once done, test out the installs:
