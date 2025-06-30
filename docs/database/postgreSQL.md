# PostgreSQL

## PostgreSQL and Docker

PostgreSQL is a powerful, open-source object-relational database system. It is a highly scalable, SQL-compliant database management system that is used to handle large workloads. PostgreSQL is a popular choice for many developers and organizations due to its robust features, extensibility, and reliability.

- you can take advantage of Docker to easily set up and run PostgreSQL on your local machine.

 Docker is a platform that allows you to package, distribute, and run applications in containers. It provides a lightweight and efficient way to run applications in isolated environments. Docker is available for Windows, macOS, and Linux, making it a versatile tool for developers.

## Docker Compose File

Now, create a new file named compose.yml in the same directory. This file will contain the configuration for your PostgreSQL container.

```yaml
services:
  db:
    image: postgres:alpine
    container_name: postgres
    restart: always
    environment:
      POSTGRES_DB: ${DB_NAME}
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    ports:
      - ${DB_PORT}:5432  # make sure you don't have another container running on DB_PORT
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -d $${DB_NAME} -U $${DB_USER}"]
      interval: 10s
      timeout: 30s
      retries: 5
    volumes:
      - ./data/db:/var/lib/postgresql/data
    attach: false

  adminer:
    image: adminer
    restart: always
    ports:
      - 8080:8080
```

- In this configuration file, we define two services: db and adminer.
- The db service is responsible for running the PostgreSQL instance, while the adminer service is responsible for running the Adminer web interface.
- It is a lightweight database management tool that allows you to interact with your databases through a web interface.

The db service uses the postgres image from the Docker Hub registry. We specify the volume mapping to store the data files in the ./data/db directory. The ports section maps the container port 5432 to the host port 5432, allowing you to access the PostgreSQL instance from your local machine.

We also set the environment variables POSTGRES_DB, POSTGRES_USER, and POSTGRES_PASSWORD to configure the database name, username, and password, respectively.

The adminer service uses the adminer image from the Docker Hub registry. We map the container port 8080 to the host port 8080 to access the Adminer web interface.

### Environment Variables

To configure the database name, username, and password, you can create a .env file in the same directory as the compose.yml file. Add the following content to the .env file:

```yaml title=".env file"
DB_NAME=chai-db
DB_USER=chaicode
DB_PASSWORD=chaiaurcode
DB_PORT=5432
```

Replace the values of DB_NAME, DB_USER, and DB_PASSWORD with your desired database name, username, and password, respectively.

### Start the PostgreSQL Container

Now that you have created the compose.yml file, you can start the PostgreSQL container by running the following command in the terminal:

```sh
docker compose up -d
```
This command will download the necessary images and start the PostgreSQL and Adminer containers in the background. You can verify that the containers are running by executing the following command:

```sh
docker ps
```
This command will display a list of running containers on your system. You should see the db and adminer containers listed in the output.

You can now access the Adminer web interface by opening a web browser and navigating to http://localhost:8080

In the login page, enter the database name, username, and password that you specified in the compose.yml file. You should now be able to interact with your PostgreSQL database through the Adminer web interface.

### Connect with PostgreSQL

If you want to connect with database url, you can use the following url:

`postgresql://chaicode:chaiaurcode@localhost:5432/chai-db`