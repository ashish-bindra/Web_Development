# Socket.IO and Celery

we used WebSockets and Broadcaster to get task status updates without server polling

## Objectives

1. Add Socket.IO support to a FastAPI application
2. Emit Socket.IO messages in a Celery worker

## Background

Socket.IO is library that simplifies the building of real-time, event-based applications.

1. Client-side - socket.io-client is a client-side library that works on top of the browser's WebSocket API
2. Server-side - python-socketio adds Socket.IO support to FastAPI

It's worth noting that while Socket.IO uses WebSockets, it adds additional metadata to each packet. Because of this you will not be able to successfully connect a regular WebSocket client with Socket.IO server.

Terminology:

1. A Namespace is a communication channel that allows you to split the logic of your application over a single shared connection (also called "multiplexing").
2. A room is an arbitrary channel that sockets can join and leave. It can be used to broadcast events to a subset of clients.


Notes:

1. We created a Class-Based Namespace, which inherits from socketio.AsyncNamespace. When the server receives a join event on the /task_status namespace, on_join handles the event.
2. on_join then adds the client to the task_id room (nearly the same as subscribing to channel) and then uses emit to send a status event to the clients in the room.
3. The register_socketio_app function mounts the AsyncServer as a FastAPI sub-application.
4. update_celery_task_status_socketio is called in the Celery worker after the task finishes.
