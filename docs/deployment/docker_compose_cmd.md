# Docker compose

repository name must be lowercase

- tool for defining and runing multi-container docker applications
- use yaml files to configure application services (docker-compose.yml)
- Can start all services with a single command: docker compose up
- Can stop all serves witha single command: docker compose doun
- CAN SCALE UP SELECTED SERVICES WHEN REQUIRED

## Docker Compose Commands

- Docker Compose is a tool for defining and running multi-container Docker applications.
- It uses a YAML file to configure the application's services, networks, and volumes.
- With a single command, you can create and start all the services from your configuration file.

## How to check docker compose version

- `DOCKER-COMPOSE -v`
- `DOCKER-COMPOSE version`
- `docker-compose -- version`

## install on linux

- `pip install -U docker-compose`

## How create docker compose file

create file with name of docker-compose.yml

- `docker-compose.yml`

## To check docker version

`docker --version`
`docker compose version`

## To find the logs

`docker compose logs -f`

## Basic Commands

1. `docker compose up`

    This command creates and starts containers as defined in the docker-compose.yml file. It can also build images before starting the containers if they do not exist.

2. `docker compose down`

    This command stops and removes containers, networks, and volumes created by docker compose up.

3. `docker compose build`

    This command builds or rebuilds services defined in the docker-compose.yml file.

4. `docker compose ps`

    This command lists all the containers in the current project.

5. `docker compose logs`

    This command displays the logs of the running services.

## Advanced Commands

6. `docker compose exec`

    This command executes a command in a running container.

    `docker compose exec <service_name> <command>`

7. `docker compose run`

    This command runs a one-off command on a service.
    `docker compose run <service_name> <command>`

8. `docker compose pull`

    This command pulls service images from a registry.

9. `docker compose push`

    This command pushes service images to a registry.

10. `docker compose restart`

    This command restarts service containers.

11. `Options and Flags`

-f, --file

Specify an alternate compose file.

`docker compose -f <file_path> up`
-p, --project-name

Specify an alternate project name.

`docker compose -p <project_name> up`
--profile

Specify a profile to enable.

`docker compose --profile <profile_name> up`
--parallel

Control the maximum level of parallelism for concurrent engine calls.

`docker compose --parallel <number> up`
--dry-run

Execute the command in dry run mode to see what would happen without making any changes.

`docker compose --dry-run up`
Docker Compose simplifies the management of multi-container applications, making it easier to develop, test, and deploy applications in various environments.

It provides a comprehensive set of commands and options to control the entire lifecycle of your application stack

```
C:\Users\Bindra\Desktop\TODO\server>mkdir dockerComposeFile

C:\Users\Bindra\Desktop\TODO\server>cd dockerComposeFile

C:\Users\Bindra\Desktop\TODO\server\dockerComposeFile>dir
 Volume in drive C has no label.
 Volume Serial Number is D82A-F854

 Directory of C:\Users\Bindra\Desktop\TODO\server\dockerComposeFile

10-10-2024  09:30    <DIR>          .
10-10-2024  09:30    <DIR>          ..
               0 File(s)              0 bytes
               2 Dir(s)   3,132,542,976 bytes free

C:\Users\Bindra\Desktop\TODO\server\dockerComposeFile>echo > docker-compose.yml
```

### edit docker-compose.yml

```
services:
  web: # name of services
    image: nginx # image
  
  databse: # other services is db
    image: redis
```

### check the validity of file by command

Also help to check validity and error

- `docker-compose config`

``` title="error"
C:\Users\Bindra\Desktop\TODO\server\dockerComposeFile>docker-compose config
validating C:\Users\Bindra\Desktop\TODO\server\dockerComposeFile\docker-compose.yml: services.web Additional property images is not allowed

```

```
C:\Users\Bindra\Desktop\TODO\server\dockerComposeFile>docker-compose config
name: dockercomposefile
services:
  database:
    image: redis
    networks:
      default: null
  web:
    image: nginx
    networks:
      default: null
networks:
  default:
    name: dockercomposefile_default
```

### start in detached mode

- `docker-compose up -d`

```
C:\Users\Bindra\Desktop\TODO\server\dockerComposeFile>docker-compose up -d
[+] Running 14/16
[+] Running 14/16⣄⣿⣿⣿⣿⣿] 20.82MB/43.8MB  Pulling            16.3s
[+] Running 14/16⣄⣿⣿⣿⣿⣿]  21.7MB/43.8MB  Pulling            16.4s
[+] Running 14/16⣄⣿⣿⣿⣿⣿]  21.7MB/43.8MB  Pulling            16.5s
[+] Running 14/16⣤⣿⣿⣿⣿⣿] 22.59MB/43.8MB  Pulling            16.6s
[+] Running 14/16⣤⣿⣿⣿⣿⣿] 23.47MB/43.8MB  Pulling            16.7s
[+] Running 14/16⣤⣿⣿⣿⣿⣿] 24.36MB/43.8MB  Pulling            16.8s
[+] Running 14/16⣤⣿⣿⣿⣿⣿] 24.36MB/43.8MB  Pulling            16.9s
[+] Running 14/16⣤⣿⣿⣿⣿⣿] 25.24MB/43.8MB  Pulling            17.0s
[+] Running 14/16⣤⣿⣿⣿⣿⣿] 26.13MB/43.8MB  Pulling            17.1s
[+] Running 14/16⣤⣿⣿⣿⣿⣿] 27.02MB/43.8MB  Pulling            17.2s
[+] Running 14/16⣤⣿⣿⣿⣿⣿] 27.02MB/43.8MB  Pulling            17.3s
[+] Running 14/16⣦⣿⣿⣿⣿⣿]  27.9MB/43.8MB  Pulling            17.4s
[+] Running 14/16⣦⣿⣿⣿⣿⣿] 28.78MB/43.8MB  Pulling            17.5s
[+] Running 14/16⣦⣿⣿⣿⣿⣿] 28.78MB/43.8MB  Pulling            17.6s
[+] Running 14/16⣦⣿⣿⣿⣿⣿] 28.78MB/43.8MB  Pulling            17.7s
[+] Running 14/16⣦⣿⣿⣿⣿⣿] 29.67MB/43.8MB  Pulling            17.8s
[+] Running 14/16⣦⣿⣿⣿⣿⣿] 29.67MB/43.8MB  Pulling            17.9s
[+] Running 14/16⣦⣿⣿⣿⣿⣿] 31.89MB/43.8MB  Pulling            18.0s
[+] Running 14/16⣶⣿⣿⣿⣿⣿] 33.22MB/43.8MB  Pulling            18.1s
[+] Running 14/16⣶⣿⣿⣿⣿⣿]  34.1MB/43.8MB  Pulling            18.2s
[+] Running 14/16⣶⣿⣿⣿⣿⣿]  34.1MB/43.8MB  Pulling            18.3s
[+] Running 14/16⣶⣿⣿⣿⣿⣿]  34.1MB/43.8MB  Pulling            18.4s
[+] Running 14/16⣶⣿⣿⣿⣿⣿] 34.99MB/43.8MB  Pulling            18.5s
[+] Running 14/16⣶⣿⣿⣿⣿⣿] 34.99MB/43.8MB  Pulling            18.6s
[+] Running 14/16⣶⣿⣿⣿⣿⣿] 35.88MB/43.8MB  Pulling            18.7s
[+] Running 14/16⣶⣿⣿⣿⣿⣿] 35.88MB/43.8MB  Pulling            18.8s
[+] Running 14/16⣶⣿⣿⣿⣿⣿]  37.2MB/43.8MB  Pulling            18.9s
[+] Running 14/16⣶⣿⣿⣿⣿⣿] 38.09MB/43.8MB  Pulling            19.0s
[+] Running 14/16⣷⣿⣿⣿⣿⣿] 38.97MB/43.8MB  Pulling            19.1s
[+] Running 14/16⣷⣿⣿⣿⣿⣿] 38.97MB/43.8MB  Pulling            19.2s
[+] Running 14/16⣷⣿⣿⣿⣿⣿] 39.41MB/43.8MB  Pulling            19.3s
[+] Running 14/16⣷⣿⣿⣿⣿⣿] 41.19MB/43.8MB  Pulling            19.4s
[+] Running 16/16⣷⣿⣿⣿⣿⣿] 42.51MB/43.8MB  Pulling            19.5s
 ✔ web 6 layers [⣿⣿⣿⣿⣿⣿]      0B/0B      Pulled             21.8s
   ✔ d07412f52e9d Pull complete                             13.7s
   ✔ 9ab66c386e9c Pull complete                              7.4s
   ✔ 4b563e5e980a Pull complete                              8.3s
   ✔ 55af3c8febf2 Pull complete                              8.7s
   ✔ 5b8e768fb22d Pull complete                              9.7s
   ✔ 85177e2c6f39 Pull complete                             10.3s
 ✔ database 8 layers [⣿⣿⣿⣿⣿⣿⣿⣿]      0B/0B      Pulled      14.1s
   ✔ 302e3ee49805 Pull complete                              5.4s
   ✔ 378d889b37dd Pull complete                              0.9s
   ✔ e4edbcee329b Pull complete                              0.9s
   ✔ c78d46bd3323 Pull complete                              4.0s
   ✔ 4b3c79aadafc Pull complete                              7.9s
   ✔ 99f3f5284f55 Pull complete                              5.5s
   ✔ 4f4fb700ef54 Pull complete                              6.6s
   ✔ 1f4a511d4985 Pull complete                              7.1s
[+] Running 2/3
 - Network dockercomposefile_default       Created           3.9s
 ✔ Container dockercomposefile-database-1  Started           3.8s
 ✔ Container dockercomposefile-web-1       Started           3.8s
```

### docker `ps` command to see the images

- `docker ps`
- `docker-compose ps`

```
C:\Users\Bindra\Desktop\TODO\server\dockerComposeFile>docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED              STATUS              PORTS      NAMES
9e3adb034705   nginx     "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp     dockercomposefile-web-1
8c8833beddf1   redis     "docker-entrypoint.s…"   About a minute ago   Up About a minute   6379/tcp   dockercomposefile-database-1
```

### top everting

```
[+] Running 3/3\Desktop\TODO\server\dockerComposeFile>docker-copos
 ✔ Container dockercomposefile-web-1       Removed           0.9s
 ✔ Container dockercomposefile-database-1  Removed           0.6s
 ✔ Network dockercomposefile_default       Removed           0.2s
operable program or batch file.
C:\Users\Bindra\Desktop\TODO\server\dockerComposeFile>
```

### Exposing the port

```
  ports:
   - "8080:80"  
```

and just check config file and run docker

```

C:\Users\Bindra\Desktop\TODO\server\dockerComposeFile>docker-compose config
name: dockercomposefile
services:
  database:
    image: redis
    networks:
      default: null
  web:
    image: nginx
    networks:
      default: null
    ports:
      - mode: ingress
        target: 80
        published: "8080"
        protocol: tcp
networks:
  default:
    name: dockercomposefile_default
[+] Running 2/3
 - Network dockercomposefile_default       Created           1.0s
 ✔ Container dockercomposefile-web-1       Started           1.0s
 ✔ Container dockercomposefile-database-1  Started           0.8s
```

vist:   <http://localhost:8080/>
![alt text](nginx.PNG)

### Bring down application by command

   docker-compose down

### Scale

- Number of container for a scervices
- Create for instance for database scerices
- `docker-compose up -d --scale database=4`

```
C:\Users\Bindra\Desktop\TODO\server\dockerComposeFile>docker-compose up -d --scale database=4
[+] Running 5/6
 - Network dockercomposefile_default       Created           2.2s
 ✔ Container dockercomposefile-web-1       Started           0.9s
 ✔ Container dockercomposefile-database-1  Started           2.2s
 ✔ Container dockercomposefile-database-3  Started           1.4s
 ✔ Container dockercomposefile-database-2  Started           1.8s
 ✔ Container dockercomposefile-database-4  Started           1.0s

```

```
C:\Users\Bindra\Desktop\TODO\server\dockerComposeFile>docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
256ba6b16b7d   redis     "docker-entrypoint.s…"   47 seconds ago   Up 46 seconds   6379/tcp               dockercomposefile-database-4
8ffa78b42263   redis     "docker-entrypoint.s…"   47 seconds ago   Up 45 seconds   6379/tcp               dockercomposefile-database-3
9eb956e2becb   redis     "docker-entrypoint.s…"   48 seconds ago   Up 45 seconds   6379/tcp               dockercomposefile-database-2
777b33730b4f   redis     "docker-entrypoint.s…"   48 seconds ago   Up 45 seconds   6379/tcp               dockercomposefile-database-1
cd1861ac5dad   nginx     "/docker-entrypoint.…"   48 seconds ago   Up 46 seconds   0.0.0.0:8080->80/tcp   dockercomposefile-web-1

```
