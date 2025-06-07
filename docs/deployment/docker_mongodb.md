# Docker for MongoDb based application

```yaml
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7


RUN apt-get update \
  && apt-get -y install gcc \
  && apt-get -y install g++ \
  && apt-get -y install unixodbc unixodbc-dev \
  && apt-get clean
RUN apt-get install libgl1 -y

RUN pip install --upgrade pip setuptools wheel
RUN pip install spacy==2.3.7
RUN python -m spacy download en_core_web_sm

COPY real.txt real.txt
# RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r real.txt
COPY ./app .
```

## docker-compose

```yaml
version: '3.7'
services:
  chatbot:
    build: .
    command: "uvicorn main_api:app --host 0.0.0.0 --port 97"
    ports:
      - "8000:97"
    restart: always
    environment: # Pass environment variables to the service
      MONGO_URI: mongodb://root:thisissomethingsecret@mongo:27017/
      APP_URL: chatbot:97

  mongo:
    image: mongo
    restart: always
    volumes:
      - ./docker_data:/data/db
    environment:
      MONGO_INITDB_ROOT_USERNAME: root
      MONGO_INITDB_ROOT_PASSWORD: thisissomethingsecret

  mongo-express:
    image: mongo-express
    restart: always
    ports:
      - 8001:8081
    environment:
      ME_CONFIG_MONGODB_ADMINUSERNAME: root
      ME_CONFIG_MONGODB_ADMINPASSWORD: thisissomethingsecret
      ME_CONFIG_MONGODB_URL: mongodb://root:thisissomethingsecret@mongo:27017/

```
