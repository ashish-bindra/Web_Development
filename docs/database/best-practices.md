# Dockerfiles

Use Multi-stage Builds

Take advantage of multi-stage builds to create leaner, more secure Docker images.

Multi-stage Docker builds allow you to break up your Dockerfiles into several stages

## Order Dockerfile Commands Appropriately

Pay close attention to the order of your Dockerfile commands to leverage layer caching.

- Docker caches each step (or layer) in a particular Dockerfile to speed up subsequent builds.
- When a step changes, the cache will be invalidated not only for that particular step but all succeeding steps.

Example:

```
FROM python:3.12.2-slim

WORKDIR /app

COPY sample.py .

COPY requirements.txt .

RUN pip install -r requirements.txt
```

In this Dockerfile, we copied over the application code before installing the requirements. Now, each time we change sample.py, the build will reinstall the packages.

his is very inefficient, especially when using a Docker container as a development environment. Therefore, it's crucial to keep the files that frequently change towards the end of the Dockerfile.

Note

You can also help prevent unwanted cache invalidations by using a .dockerignore file to exclude unnecessary files from being added to the Docker build context and the final image

```
FROM python:3.12.2-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY sample.py .
```

1. Always put layers that are likely to change as low as possible in the Dockerfile.
2. Combine RUN apt-get update and RUN apt-get install commands. (This also helps to reduce the image size. We'll touch on this shortly.)
3. If you want to turn off caching for a particular Docker build, add the --no-cache=True flag.

## Use Small Docker Base Images

Smaller Docker images are more modular and secure.

Building, pushing, and pulling images is quicker with smaller images.

- They also tend to be more secure since they only include the necessary libraries and system dependencies required for running your application.

```
REPOSITORY   TAG                    IMAGE ID         CREATED          SIZE
python       3.12.2-bookworm        939b824ad847     40 hours ago     1.02GB
python       3.12.2-slim            24c52ee82b5c     40 hours ago     130MB
python       3.12.2-slim-bookworm   24c52ee82b5c     40 hours ago     130MB
python       3.12.2-alpine          c54b53ca8371     40 hours ago     51.8MB
python       3.12.2-alpine3.19      c54b53ca8371     40 hours ago     51.8MB
```

While the Alpine flavor, based on Alpine Linux, is the smallest, it can often lead to increased build times if you can't find compiled binaries that work with it. As a result, you may end up having to build the binaries yourself, which can increase the image size (depending on the required system-level dependencies) and the build times (due to having to compile from the source).

 Using Alpine can make Python Docker builds 50× slower

 <https://pythonspeed.com/articles/alpine-docker-python/>

 *-slim flavor, especially in development mode, as you're building your application. You want to avoid having to continually update the Dockerfile to install necessary system-level dependencies when you add a new Python package.

  don't forget to update your base images regularly to improve security and boost performance. When a new version of a base image is released -- e.g., 3.11.8-slim -> 3.12.2-slim -- you should pull the new image and update your running containers to get all the latest security patches.

## Minimize the Number of Layers

- It's a good idea to combine the RUN, COPY, and ADD commands as much as possible since they create layers.
- Each layer increases the size of the image since they are cached.
- as the number of layers increases, the size also increases.

You can test this out with the docker history command:

```
docker images
REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
dockerfile   latest    180f98132d02   51 seconds ago   259MB

$ docker history 180f98132d02

IMAGE          CREATED              CREATED BY                                      SIZE      COMMENT
180f98132d02   58 seconds ago       COPY . . # buildkit                             6.71kB    buildkit.dockerfile.v0
<missing>      58 seconds ago       RUN /bin/sh -c pip install -r requirements.t…   35.5MB    buildkit.dockerfile.v0
<missing>      About a minute ago   COPY requirements.txt . # buildkit              58B       buildkit.dockerfile.v0
<missing>      About a minute ago   WORKDIR /app
...
```

Take note of the sizes. Only the RUN, COPY, and ADD commands add size to the image. You can reduce the image size by combining commands wherever possible. For example:

```
RUN apt-get update
RUN apt-get install -y netcat
```

Can be combined into a single RUN command:

```
RUN apt-get update && apt-get install -y netcat
```

Thus, creating a single layer instead of two, which reduces the size of the final image.

In other words, focus more on the previous three practices -- multi-stage builds, order of your Dockerfile commands, and using a small base image -- than trying to optimize every single command.

Notes:

1. RUN, COPY, and ADD each create layers.
2. Each layer contains the differences from the previous layer.
3. Layers increase the size of the final image

Tips:

1. Combine related commands.
2. Remove unnecessary files in the same RUN step that created them.
3. Minimize the number of times apt-get upgrade is run since it upgrades all packages to the latest version.
4. With multi-stage builds, don't worry too much about overly optimizing the commands in temp stages.

Finally, for readability, it's a good idea to sort multi-line arguments alphanumerically

```
RUN apt-get update && apt-get install -y \
    git \
    gcc \
    matplotlib \
    pillow  \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
```

it's crucial to perform clean-up actions within the same RUN instruction to avoid unnecessary bloat in your Docker images

This approach ensures that temporary files or cache used during installation are not included in the final image layer, effectively reducing the image size.

For example, after installing packages with apt-get, use && apt-get clean && rm -rf /var/lib/apt/lists/* to remove the package lists and any temporary files created during the installation process, as demonstrated above

## Use Unprivileged Containers

Docker runs container processes as root inside of a container. However, this is a bad practice since a process running as root inside the container is running as root in the Docker host.

if an attacker gains access to your container, they have access to all the root privileges and can perform several attacks against the Docker host, like-

1. copying sensitive info from the host's filesystem to the container
2. executing remote commands

To prevent this, make sure to run container processes with a non-root user:

```
RUN addgroup --system app && adduser --system --group app

USER app
```

You can take it a step further and remove shell access and ensure there's no home directory as well:

```yaml
RUN addgroup --gid 1001 --system app && \
    adduser --no-create-home --shell /bin/false --disabled-password --uid 1001 --system --group app

USER app
```

Verify:

```
docker run -i sample id

uid=1001(app) gid=1001(app) groups=1001(app)
```

the Docker daemon and the container itself still run with root privileges. Be sure to review Run the Docker daemon as a non-root user for help with running both the daemon and containers as a non-root user.

## Prefer COPY Over ADD

Use COPY unless you're sure you need the additional functionality that comes with ADD.

### What's the difference between COPY and ADD?

Both commands allow you to copy files from a specific location into a Docker image:

```
ADD <src> <dest>
COPY <src> <dest>
```

While they look like they serve the same purpose, ADD has some additional functionality:

- COPY is used for copying local files or directories from the Docker host to the image.
- ADD can be used for the same thing as well as downloading external files. Also, if you use a compressed file (tar, gzip, bzip2, etc.) as the <src> parameter, ADD will automatically unpack the contents to the given location.

```
# copy local files on the host to the destination
COPY /source/path  /destination/path
ADD /source/path  /destination/path

# download external file and copy to the destination
ADD http://external.file/url  /destination/path

# copy and extract local compresses files
ADD source.file.tar.gz /destination/path
```

## Cache Python Packages to the Docker Host

When a requirements file is changed, the image needs to be rebuilt to install the new packages. The earlier steps will be cached, as mentioned in Minimize the Number of Layers. Downloading all packages while rebuilding the image can cause a lot of network activity and takes a lot of time. Each rebuild takes up the same amount of time for downloading common packages across builds.

You can avoid this by mapping the pip cache directory to a directory on the host machine. So for each rebuild, the cached versions persist and can improve the build speed.

Add a volume to the docker run as -v $HOME/.cache/pip-docker/:/root/.cache/pip or as a mapping in the Docker Compose file.

The directory presented above is only for reference. Make sure you map the cache directory and not the site-packages (where the built packages reside).

Moving the cache from the docker image to the host can save you space in the final image.

If you're leveraging Docker BuildKit, use BuildKit cache mounts to manage the cache:

```
COPY requirements.txt .

RUN --mount=type=cache,target=/root/.cache/pip \
        pip install -r requirements.txt
```

## Run Only One Process Per Container

Why is it recommended to run only one process per container?

Let's assume your application stack consists of a two web servers and a database. While you could easily run all three from a single container, you should run each in a separate container to make it easier to reuse and scale each of the individual services.

1. Scaling - With each service in a separate container, you can scale one of your web servers horizontally as needed to handle more traffic.
2. Reusability - Perhaps you have another service that needs a containerized database. You can simply reuse the same database container without bringing two unnecessary services along with it.
3. Portability and Predictability - It's much easier to make security patches or debug an issue when there's less surface area to work with.

## Prefer Array Over String Syntax

You can write the `CMD` and `ENTRYPOINT` commands in your Dockerfiles in both array (exec) or string (shell) formats:

