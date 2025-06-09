# celery - Distributed Task Queue

It's a task quese with focus on realtime processing, while also supporting task scheduling

> Most popular task queue in python

you can return an HTTP response back immediately and run the process as a background task, instead of forcing the user to wait for the task finish.

## Celery vs FastAPI's BackgroundTasks

when should you use Celery instead of BackgroundTasks?

1. CPU intensive tasks:

    Celery should be used for tasks that perform heavy background computations since BackgroundTasks runs in the same event loop that serves your app's requests.
2. Task queue:

    If you require a task queue to manage the tasks and workers, you should use Celery. Often you'll want to retrieve the status of a job and then perform some action based on the status -- i.e., send an error email, kick off a different background task, or retry the task. Celery manages all this for you

Notes:

    1. After creating a FastAPI instance, we created a new instance of Celery.
    2. The broker and backend tells Celery to use the Redis service we just launched.
    3. Rather than hard-coding these values, you can define them in a separate config file or pull them from environment variables.
    4. We defined a Celery task called divide, which simulates a long-running task.
Sending a Task to Celery

## What is task queue

Task is a way for you to offload time instensive, process instensive or unreliable task to a separate process so our main process does not get block.

- Need a driver for the task queue or the broker that we will use
- ![alt text](img/celery.png)
- celery will list the task a to figer out what need to be run.

## Radis

Radis is an in-memory database storage

## install celery

- `pip install celery`

## install radis

- `pip install radis`

For actual radis instese we used docker compose

```

```

## IN-memory Database

An in-memory database is a purpose-built database that primarily relies on internal memory (RAM) for data storage. This eliminates the need to access standard disk drives, resulting in minimal response times.

In-memory databases are ideal for applications requiring microsecond response times or handling large spikes in traffic, such as gaming leaderboards, session stores, and real-time data analytics

### Common Use Cases

- Real-Time Analytics: Quick analysis of large datasets, such as fraud detection systems

- Session Storage: Maintaining user session information in web applications

- Gaming Leaderboards: Quickly delivering sorting results and updating leaderboards in real-time for games with millions of players

# Run file like regular function

`python -i task.py`

## To start the celery

`celery -A task worker -l info`

for windows

`celery -A task worker --pool=solo -l info`

celery -A app.celery_worker.celery worker --loglevel=info

celery -A main.celery worker --loglevel=info
