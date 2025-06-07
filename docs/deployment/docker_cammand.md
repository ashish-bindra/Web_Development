# DockerFile

Docker makes the process of application deployment very easy and efficient and resolves a lot of issues relatged to deploymeimg apllications.

- Docker is world's leading softwarecontainer platform.
- Docker is a tool designed to make it easier to deploy and run

## applications by using containers

- Containers allow a developer to package up an application with all of the parts it needs, such as libraries and other depencies, and ship it all out as ope pakage.

## Dockerfile

- Describes steps to create a Docker image. It's like a recipe with all ingreients and steps necessary in making your dish.
- container will have application with all its dependencies.

The daemon (server) receives the commands from the Docker client through CLI or REST API's

## Build app only once (relise 2013)

An application inside a cotainer can run on any system that has Docker installed.So there is no need to bld a configure app multiple times on different platform.

## Docker Basic Commands

### Basic

- docker version: information of version of docker client and docker server
- docker -v: version of docker
- docker info: detail information of docker (img,cotainer all thing)

- docker --help
- docker login

### images

- docker images
- docker pull
- docker rmi: remove one or more images

### container

- docekr ps
- docker run
- docker start
- docker stop

### System

- docker stats: check the memory usage
- docekr system df: check the disk usage
- docker system prune: docker system

dagling means images which are not associate with running conatiner

- A dangling image is one that is not tagged and is not referenced by any container.

## docker images

Docker imges are templates used to create Docker container

- Container is a runiing instace of images

- docker images --help
- docker pull image
- docker images
- docker images - q
- docker images - f "dangling=false"
- docker images - f "dangling=false" -q

- docker run images
- docker rmi image
- docker emo -f image
- docker inspect

image typically contains a unuion of layered files systems stacked on top of each other.

## Docker image with Uvicorn and Gunicorn for FastAPI apps

[uvicorn-gunicorn-fastapi] +
(<https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker/tree/master/docker-images>)

## Dockerfile Commands

1. **docker build -t myimage .**
   - To Build the Docker Image

2. **docker run -d --name mycontainer -p 80:80 myimage**
   - Start the Docker Container

3. **docker images**
   - List images by name and tag

4. **docker load < busybox.tar.gz**
   - To Load an image from a tar archive or STDIN

5. **docker image save -o busybox.tar imageName**
   - To save an image in .tar format

6. **docker rmi -f image name or ID**
   - To remove docker image forcefully

----

## docker compose

```yaml
version: '3'  # This defines the version of the Docker Compose format being used.

services:     # This section defines the services (containers) that will be created.
   app:          # The name of the service (in this case, 'app').
      build:     # Specifies that the service should be built using a Dockerfile.
         context: .               # The context specifies the build directory (here, the current directory).
         dockerfile: Dockerfile   # The name of the Dockerfile to be used for building the image.
      ports:
         - "89:89"  # Maps port 89 of the host to port 89 of the container.
```

## Commands

### 1. If you modified the Docker Compose configuration (docker-compose.yml)

`docker-compose up -d --build`

### 2. If you only modified a service's code or configuration files (not the docker-compose.yml)

You can simply restart the service without rebuilding the image:

`docker-compose restart <service-name>`

### 3. If you made code changes that require rebuilding the image

docker-compose build <service-name>

> image name is service name read in docker-compose file

### If you want to rebuild all services

`docker-compose build`

### After rebuilding, restart the containers

`docker-compose up -d`

### Stop services only

`docker-compose stop`

### Stop and remove containers, networks

`docker-compose down`

### Down and remove volumes

`docker-compose down --volumes`

### Down and remove images

`docker-compose down --rmi <all|local>`
